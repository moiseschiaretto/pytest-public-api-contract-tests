import allure
from src.services.auth_service import AuthService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data
from src.config.environment import environment


# POST /auth/login - senha incorreta retorna 400
@allure.title('POST /auth/login - status 400')
def test_post_auth_login_status_400():
    folder_path = 'public-api/auth/POST/400'
    auth_service = AuthService()

    response, response_data = auth_service.post_login(
        body={
            'username': environment.api.username,
            'password': environment.api.password_invalid
        },
        expected_status=400,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
