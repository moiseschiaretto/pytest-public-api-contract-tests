from src.config.endpoints import ENDPOINT_QUOTES, ENDPOINT_QUOTES_RANDOM
from src.services.base_service import BaseService


# Serviço de citações: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class QuoteService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_QUOTES)

    # GET /quotes/random
    def get_random(self, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=ENDPOINT_QUOTES_RANDOM,
            expected_status=expected_status,
            save_response_log=save_response_log
        )
