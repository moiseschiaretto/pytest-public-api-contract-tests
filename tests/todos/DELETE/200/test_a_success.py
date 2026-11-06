import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# DELETE /todos/{id} - simula exclusão de tarefa
@allure.title('DELETE /todos/1 - status 200')
def test_delete_todos_status_200():
    folder_path = 'public-api/todos/DELETE/200'
    todo_service = TodoService()

    response, response_data = todo_service.delete_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['isDeleted'] is True
