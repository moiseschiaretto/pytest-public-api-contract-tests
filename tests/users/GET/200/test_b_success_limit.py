import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /users?limit=5&skip=10 - paginação
@allure.title('GET /users - status 200')
def test_get_users_limit_status_200():
    folder_path = 'public-api/users/GET/200'
    user_service = UserService()

    response, response_data = user_service.get_all(
        query={'limit': 5, 'skip': 10},
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.limit.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
