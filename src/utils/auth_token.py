# Autentica na API pública DummyJSON e guarda o accessToken em cache local
# (.token-cache.json, fora do versionamento) para os testes reutilizarem.
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()


def refresh_token():
    base_url = os.getenv('API_BASE_URL') or 'https://dummyjson.com'
    username = os.getenv('AUTH_USERNAME') or 'emilys'
    password = os.getenv('AUTH_PASSWORD') or 'emilyspass'

    print(f'🔑 Autenticando na DummyJSON como "{username}"...')

    response = requests.post(
        f'{base_url}/auth/login',
        json={'username': username, 'password': password, 'expiresInMins': 60},
        timeout=15
    )

    if not response.ok:
        raise RuntimeError(f'Falha ao autenticar: HTTP {response.status_code}')

    data = response.json()
    cache_path = Path.cwd() / '.token-cache.json'
    cache_path.write_text(json.dumps({'accessToken': data['accessToken'], 'obtainedAt': datetime.now(timezone.utc).isoformat()}, indent=2), encoding='utf-8')

    print('✅ Token obtido e salvo em .token-cache.json')
    return data['accessToken']


if __name__ == '__main__':
    try:
        refresh_token()
    except Exception as error:
        print(f'❌ Erro ao obter token: {error}')
        sys.exit(1)
