import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /users/{id} - usuário inexistente retorna 404
@allure.title('GET /users/999999 - status 404')
def test_get_users_status_404():
    folder_path = 'public-api/users/GET/404'
    user_service = UserService()

    response, response_data = user_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
