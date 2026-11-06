import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# PUT /users/{id} - simula atualização de usuário
@allure.title('PUT /users/1 - status 200')
def test_put_users_status_200():
    folder_path = 'public-api/users/PUT/200'
    body = load_json_fixture('resources/fixtures/public-api/users/PUT/request/valid.json')
    user_service = UserService()

    response, response_data = user_service.put_id(
        1,
        body=body,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['firstName'] == body['firstName']
