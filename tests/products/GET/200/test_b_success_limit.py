import allure
from src.services.product_service import ProductService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /products?limit=5 - paginação com limit e skip
@allure.title('GET /products - status 200')
def test_get_products_limit_status_200():
    folder_path = 'public-api/products/GET/200'
    product_service = ProductService()

    response, response_data = product_service.get_all(
        query={'limit': 5, 'skip': 10},
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.limit.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
