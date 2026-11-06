import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /users/add - simula criação de usuário
@allure.title('POST /users/add - status 201')
def test_post_users_add_status_201():
    folder_path = 'public-api/users/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/users/POST/request/valid.json')
    user_service = UserService()

    response, response_data = user_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['firstName'] == body['firstName']
