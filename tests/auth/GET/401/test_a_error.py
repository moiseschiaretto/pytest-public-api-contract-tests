import allure
from src.services.auth_service import AuthService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /auth/me - sem token retorna 401
@allure.title('GET /auth/me - status 401')
def test_get_auth_me_status_401():
    folder_path = 'public-api/auth/GET/401'
    auth_service = AuthService()

    response, response_data = auth_service.get_me(
        token=None,
        expected_status=401,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
