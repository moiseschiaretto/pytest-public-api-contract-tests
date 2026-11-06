import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /carts/{id} - carrinho único
@allure.title('GET /carts/1 - status 200')
def test_get_carts_single_status_200():
    folder_path = 'public-api/carts/GET/200'
    cart_service = CartService()

    response, response_data = cart_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
