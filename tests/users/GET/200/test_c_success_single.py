import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /users/{id} - usuário único
@allure.title('GET /users/1 - status 200')
def test_get_users_single_status_200():
    folder_path = 'public-api/users/GET/200'
    user_service = UserService()

    response, response_data = user_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'c.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
