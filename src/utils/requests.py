import json
import requests
from src.utils.files import save_response_to_file

REQUEST_TIMEOUT = 15


# Função única para todos os métodos HTTP: monta cabeçalhos, envia, confere o status e salva o log
def make_request(method, base_url, end_point, expected_status, token=None, body=None, headers=None, validate_status=True, show_response_log=False, save_response_log=None):
    try:
        default_headers = {'Accept': 'application/json'}
        if token:
            default_headers['Authorization'] = f'Bearer {token}'
        if body:
            default_headers['Content-Type'] = 'application/json'

        final_headers = {**default_headers, **(headers or {})}

        response = requests.request(
            method=method.upper(),
            url=f'{base_url}{end_point}',
            headers=final_headers,
            json=body if body else None,
            timeout=REQUEST_TIMEOUT
        )

        if validate_status:
            assert response.status_code == expected_status, f'Status esperado {expected_status}, recebido {response.status_code} em {method} {end_point}'

        response_data = response.json()

        if show_response_log:
            print('\n=== RESPONSE LOG ===')
            print(f'{method} {base_url}{end_point}')
            print(f'Status: {response.status_code}')
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
            print('==================\n')

        if save_response_log:
            save_response_to_file(response_data, save_response_log)

        return response, response_data

    except Exception as error:
        print(f'Erro ao realizar a requisição {method}: {error}')
        raise
