import allure
from src.services.auth_service import AuthService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /auth/me - retorna dados do usuário autenticado
@allure.title('GET /auth/me - status 200')
def test_get_auth_me_status_200():
    folder_path = 'public-api/auth/GET/200'
    auth_service = AuthService()

    response, response_data = auth_service.get_me(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
