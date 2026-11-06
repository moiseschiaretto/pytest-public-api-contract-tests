import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /carts/{id} - carrinho inexistente retorna 404
@allure.title('GET /carts/999999 - status 404')
def test_get_carts_status_404():
    folder_path = 'public-api/carts/GET/404'
    cart_service = CartService()

    response, response_data = cart_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
