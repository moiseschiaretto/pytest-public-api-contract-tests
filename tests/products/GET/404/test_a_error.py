import allure
from src.services.product_service import ProductService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /products/{id} - produto inexistente retorna 404
@allure.title('GET /products/999999 - status 404')
def test_get_products_status_404():
    folder_path = 'public-api/products/GET/404'
    product_service = ProductService()

    response, response_data = product_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
