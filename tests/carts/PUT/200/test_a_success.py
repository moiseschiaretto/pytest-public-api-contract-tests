import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# PUT /carts/{id} - simula atualização de carrinho
@allure.title('PUT /carts/1 - status 200')
def test_put_carts_status_200():
    folder_path = 'public-api/carts/PUT/200'
    body = load_json_fixture('resources/fixtures/public-api/carts/PUT/request/valid.json')
    cart_service = CartService()

    response, response_data = cart_service.put_id(
        1,
        body=body,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
