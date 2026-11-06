from urllib.parse import urlencode
from src.config.environment import environment
from src.utils.requests import make_request


# Classe base de todos os serviços (Page Object Model de API).
# Cada recurso da API (produtos, usuários, carrinhos...) tem o seu serviço,
# que herda daqui os métodos HTTP padrão: post, get_all, get_id, put_id, patch_id e delete_id.
# Leitura (GET) vai sem token; escrita (POST, PUT, PATCH, DELETE) vai com o token do ambiente.
class BaseService:
    def __init__(self, end_point, end_point_add=None):
        self.end_point = end_point
        self.end_point_add = end_point_add or end_point

    # Único ponto que chama o make_request: todos os métodos passam por aqui
    def send(self, method, end_point, expected_status, save_response_log=None, body=None, token=None):
        return make_request(
            method=method,
            base_url=environment.api.base_url,
            end_point=end_point,
            token=token,
            body=body,
            expected_status=expected_status,
            show_response_log=False,
            save_response_log=save_response_log
        )

    # Monta a query string a partir de um dicionário, ex.: {'limit': 5} -> "?limit=5"
    def build_query(self, query):
        return f'?{urlencode(query)}' if query else ''

    # POST /{recurso}/add
    def post(self, body, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='POST',
            end_point=self.end_point_add,
            body=body,
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # GET /{recurso}
    def get_all(self, expected_status, save_response_log=None, query=None, token=None):
        return self.send(
            method='GET',
            end_point=f'{self.end_point}{self.build_query(query)}',
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # GET /{recurso}/{id}
    def get_id(self, id, expected_status, save_response_log=None, token=None):
        return self.send(
            method='GET',
            end_point=f'{self.end_point}/{id}',
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # PUT /{recurso}/{id}
    def put_id(self, id, body, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='PUT',
            end_point=f'{self.end_point}/{id}',
            body=body,
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # PATCH /{recurso}/{id}
    def patch_id(self, id, body, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='PATCH',
            end_point=f'{self.end_point}/{id}',
            body=body,
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # DELETE /{recurso}/{id}
    def delete_id(self, id, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='DELETE',
            end_point=f'{self.end_point}/{id}',
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )
