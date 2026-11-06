# Carrega as variáveis de ambiente do arquivo .env
import json
import os
from pathlib import Path
from types import SimpleNamespace
from dotenv import load_dotenv

load_dotenv()


# O token é atualizado por "python -m src.utils.auth_token" (src/utils/auth_token.py)
# e fica em cache local (.token-cache.json, fora do versionamento) para não precisar
# reescrever o .env a cada execução.
def load_cached_token():
    cache_path = Path.cwd() / '.token-cache.json'
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding='utf-8')).get('accessToken')
        except (ValueError, OSError):
            return None
    return None


environment = SimpleNamespace(
    api=SimpleNamespace(
        base_url=os.getenv('API_BASE_URL') or 'https://dummyjson.com',
        username=os.getenv('AUTH_USERNAME') or 'emilys',
        password=os.getenv('AUTH_PASSWORD') or 'emilyspass',
        token=load_cached_token() or os.getenv('ACCESS_TOKEN') or '',
        token_invalid='token-invalido-de-propósito-para-teste-negativo',
        password_invalid='senha-errada-de-proposito'
    )
)
