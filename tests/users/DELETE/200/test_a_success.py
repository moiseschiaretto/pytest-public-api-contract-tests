import allure
from src.services.user_service import UserService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# DELETE /users/{id} - simula exclusão de usuário
@allure.title('DELETE /users/1 - status 200')
def test_delete_users_status_200():
    folder_path = 'public-api/users/DELETE/200'
    user_service = UserService()

    response, response_data = user_service.delete_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['isDeleted'] is True
