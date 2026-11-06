import allure
from src.services.cart_service import CartService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# DELETE /carts/{id} - simula exclusão de carrinho
@allure.title('DELETE /carts/1 - status 200')
def test_delete_carts_status_200():
    folder_path = 'public-api/carts/DELETE/200'
    cart_service = CartService()

    response, response_data = cart_service.delete_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['isDeleted'] is True
