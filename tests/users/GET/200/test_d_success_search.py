import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /users/search?q= - busca por termo
@allure.title('GET /users/search - status 200')
def test_get_users_search_status_200():
    folder_path = 'public-api/users/GET/200'
    user_service = UserService()

    response, response_data = user_service.get_search(
        'John',
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'd.success.search.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
