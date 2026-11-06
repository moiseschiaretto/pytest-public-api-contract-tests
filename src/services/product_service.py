from src.config.endpoints import ENDPOINT_PRODUCTS, ENDPOINT_PRODUCTS_ADD, ENDPOINT_PRODUCTS_SEARCH, ENDPOINT_PRODUCTS_CATEGORIES, ENDPOINT_PRODUCTS_BY_CATEGORY
from src.services.base_service import BaseService


# Serviço de produtos: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class ProductService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_PRODUCTS, ENDPOINT_PRODUCTS_ADD)

    # GET /products/search?q={termo}
    def get_search(self, term, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=f"{ENDPOINT_PRODUCTS_SEARCH}{self.build_query({'q': term})}",
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # GET /products/categories
    def get_categories(self, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=ENDPOINT_PRODUCTS_CATEGORIES,
            expected_status=expected_status,
            save_response_log=save_response_log
        )

    # GET /products/category/{category}
    def get_by_category(self, category, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=ENDPOINT_PRODUCTS_BY_CATEGORY.replace('{category}', category),
            expected_status=expected_status,
            save_response_log=save_response_log
        )
