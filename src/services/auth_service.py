from src.config.endpoints import ENDPOINT_AUTH_LOGIN, ENDPOINT_AUTH_ME
from src.config.environment import environment
from src.services.base_service import BaseService


# Serviço de autenticação: /auth/login e /auth/me
class AuthService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_AUTH_LOGIN)

    # POST /auth/login
    def post_login(self, body, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='POST',
            end_point=ENDPOINT_AUTH_LOGIN,
            body=body,
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # GET /auth/me
    def get_me(self, expected_status, save_response_log=None, token=environment.api.token):
        return self.send(
            method='GET',
            end_point=ENDPOINT_AUTH_ME,
            token=token,
            expected_status=expected_status,
            save_response_log=save_response_log
        )
