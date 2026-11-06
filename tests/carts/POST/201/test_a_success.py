import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /carts/add - simula criação de carrinho
@allure.title('POST /carts/add - status 201')
def test_post_carts_add_status_201():
    folder_path = 'public-api/carts/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/carts/POST/request/valid.json')
    cart_service = CartService()

    response, response_data = cart_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
