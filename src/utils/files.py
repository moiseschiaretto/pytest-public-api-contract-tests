import json
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']


def clear_directory(directory):
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True, exist_ok=True)


def save_response_to_file_detailed(response_data, file_name, directory):
    local_date = datetime.now(ZoneInfo('America/Sao_Paulo'))
    formatted_date = local_date.strftime('%d%m%Y_%H%M')
    full_path = directory / f'{file_name}_{formatted_date}.json'

    directory.mkdir(parents=True, exist_ok=True)
    full_path.write_text(json.dumps(response_data, indent=2, ensure_ascii=False), encoding='utf-8')


# Salva a resposta em logs/{folder_path}/{recurso}_{MÉTODO}_{status}_{ddmmaaaa_hhmm}.json
def save_response_to_file(response_data, folder_path):
    file_path = Path.cwd() / 'logs' / folder_path
    path_parts = folder_path.split('/')

    method = next((part for part in path_parts if part in HTTP_METHODS), 'UNKNOWN')
    status = next((part for part in reversed(path_parts) if part.isdigit()), 'status')
    status_index = path_parts.index(status) if status in path_parts else -1
    resource = path_parts[status_index - 1] if status_index > 0 else (path_parts[-2] if len(path_parts) > 1 else 'resource')

    file_name = f'{resource}_{method}_{status}'
    clear_directory(file_path)
    save_response_to_file_detailed(response_data, file_name, file_path)


# Carrega o body da requisição, ex.: resources/fixtures/public-api/products/POST/request/valid.json
def load_json_fixture(relative_path):
    json_file_path = Path.cwd() / relative_path
    return json.loads(json_file_path.read_text(encoding='utf-8'))


# Carrega o contrato esperado, ex.: resources/fixtures/public-api/products/POST/201/a.success.json
def load_expected_data(folder_path, filename):
    if not filename:
        raise ValueError('O parâmetro filename é obrigatório para load_expected_data')
    json_path = Path.cwd() / 'resources/fixtures' / folder_path / filename
    return json.loads(json_path.read_text(encoding='utf-8'))
