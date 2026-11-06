import allure
from src.services.auth_service import AuthService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data
from src.config.environment import environment


# POST /auth/login - autenticação válida retorna accessToken
@allure.title('POST /auth/login - status 200')
def test_post_auth_login_status_200():
    folder_path = 'public-api/auth/POST/200'
    auth_service = AuthService()

    response, response_data = auth_service.post_login(
        body={
            'username': environment.api.username,
            'password': environment.api.password,
            'expiresInMins': 60
        },
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert 'accessToken' in response_data
    assert isinstance(response_data['accessToken'], str)
