from src.config.endpoints import ENDPOINT_TODOS, ENDPOINT_TODOS_ADD, ENDPOINT_TODOS_RANDOM
from src.services.base_service import BaseService


# Serviço de tarefas: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class TodoService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_TODOS, ENDPOINT_TODOS_ADD)

    # GET /todos/random
    def get_random(self, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=ENDPOINT_TODOS_RANDOM,
            expected_status=expected_status,
            save_response_log=save_response_log
        )
