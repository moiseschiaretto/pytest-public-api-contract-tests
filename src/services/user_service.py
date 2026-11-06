from src.config.endpoints import ENDPOINT_USERS, ENDPOINT_USERS_ADD, ENDPOINT_USERS_SEARCH
from src.services.base_service import BaseService


# Serviço de usuários: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class UserService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_USERS, ENDPOINT_USERS_ADD)

    # GET /users/search?q={termo}
    def get_search(self, term, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=f"{ENDPOINT_USERS_SEARCH}{self.build_query({'q': term})}",
            expected_status=expected_status,
            save_response_log=save_response_log
        )
