from src.config.endpoints import ENDPOINT_RECIPES, ENDPOINT_RECIPES_SEARCH
from src.services.base_service import BaseService


# Serviço de receitas: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class RecipeService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_RECIPES)

    # GET /recipes/search?q={termo}
    def get_search(self, term, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=f"{ENDPOINT_RECIPES_SEARCH}{self.build_query({'q': term})}",
            expected_status=expected_status,
            save_response_log=save_response_log
        )
