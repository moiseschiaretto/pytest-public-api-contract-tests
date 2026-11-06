import allure
from src.services.product_service import ProductService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /products/add - simula criação de produto
@allure.title('POST /products/add - status 201')
def test_post_products_add_status_201():
    folder_path = 'public-api/products/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/products/POST/request/valid.json')
    product_service = ProductService()

    response, response_data = product_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['title'] == body['title']
