import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /carts - lista paginada de carrinhos
@allure.title('GET /carts - status 200')
def test_get_carts_status_200():
    folder_path = 'public-api/carts/GET/200'
    cart_service = CartService()

    response, response_data = cart_service.get_all(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
