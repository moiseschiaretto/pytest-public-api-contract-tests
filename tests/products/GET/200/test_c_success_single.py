import allure
from src.services.product_service import ProductService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /products/{id} - produto único
@allure.title('GET /products/1 - status 200')
def test_get_products_single_status_200():
    folder_path = 'public-api/products/GET/200'
    product_service = ProductService()

    response, response_data = product_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'c.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
