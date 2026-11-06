import allure
from src.services.product_service import ProductService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# PUT /products/{id} - simula atualização de produto
@allure.title('PUT /products/1 - status 200')
def test_put_products_status_200():
    folder_path = 'public-api/products/PUT/200'
    body = load_json_fixture('resources/fixtures/public-api/products/PUT/request/valid.json')
    product_service = ProductService()

    response, response_data = product_service.put_id(
        1,
        body=body,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['title'] == body['title']
