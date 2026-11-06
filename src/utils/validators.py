import re
from datetime import datetime
from urllib.parse import urlparse
from jsonschema import Draft7Validator, FormatChecker

ISO_DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')

format_checker = FormatChecker()


# Formatos aceitam texto vazio, como no contrato original
@format_checker.checks('date-time')
def is_date_time(value):
    if not isinstance(value, str) or value == '':
        return True
    try:
        datetime.fromisoformat(value.replace('Z', '+00:00'))
        return True
    except ValueError:
        return False


@format_checker.checks('uri')
def is_uri(value):
    if not isinstance(value, str) or value == '':
        return True
    parsed = urlparse(value)
    return bool(parsed.scheme and parsed.netloc)


# FUNÇÃO PRINCIPAL — teste de contrato baseado em schema (tipos, não valores exatos)
# Ideal para APIs públicas, cujos dados mudam mas cuja ESTRUTURA se mantém estável.
def validate_response_with_json_schema(response_data, expected_json, validation_mode='allow-extra'):
    allow_extra = validation_mode != 'exact-schema'
    schema = generate_json_schema(expected_json, allow_extra)

    errors = sorted(Draft7Validator(schema, format_checker=format_checker).iter_errors(response_data), key=lambda e: list(e.path))

    if errors:
        details = ', '.join(f"{'.'.join(str(p) for p in error.path) or 'raiz'}: {error.message}" for error in errors)
        print(f'❌ Falha na validação de contrato: {details}')
        raise AssertionError(f'Erro de validação de contrato: {details}')

    print('✅ Contrato validado com sucesso (schema/tipos conferem)')
    return response_data


# Gera o JSON Schema a partir de uma amostra (o arquivo de contrato esperado).
# Inteiro e decimal valem como "number": em APIs públicas o mesmo campo (ex.: total)
# pode vir inteiro numa amostra e decimal na próxima.
def generate_json_schema(sample, allow_extra):
    if isinstance(sample, bool):
        return {'type': 'boolean'}
    if isinstance(sample, (int, float)):
        return {'type': 'number'}
    if isinstance(sample, str):
        schema = {'type': 'string'}
        if ISO_DATE_PATTERN.match(sample):
            schema['format'] = 'date-time'
        if sample.startswith('http'):
            schema['format'] = 'uri'
        return schema
    if isinstance(sample, list):
        if not sample:
            return {'type': 'array'}
        return {'type': 'array', 'items': merge_schemas([generate_json_schema(item, allow_extra) for item in sample])}
    if isinstance(sample, dict):
        return {'type': 'object', 'properties': {key: generate_json_schema(value, allow_extra) for key, value in sample.items()}, 'additionalProperties': allow_extra}
    return {}


# Une os schemas dos itens de uma lista: objetos somam os campos; tipos diferentes viram "qualquer valor"
def merge_schemas(schemas):
    first = schemas[0]
    if any(schema.get('type') != first.get('type') for schema in schemas):
        return {}
    if first.get('type') != 'object':
        return first
    properties = {}
    for schema in schemas:
        for key, value in schema['properties'].items():
            properties[key] = merge_schemas([properties[key], value]) if key in properties else value
    return {**first, 'properties': properties}


# Validação exata (para campos estáveis, ex.: mensagens de erro conhecidas, status)
def validate_response(response_data, expected_structure):
    for key, value in expected_structure.items():
        assert response_data.get(key) == value, f'Campo "{key}": esperado {value!r}, recebido {response_data.get(key)!r}'
