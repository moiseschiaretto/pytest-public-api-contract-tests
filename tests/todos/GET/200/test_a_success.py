import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /todos - lista paginada de tarefas
@allure.title('GET /todos - status 200')
def test_get_todos_status_200():
    folder_path = 'public-api/todos/GET/200'
    todo_service = TodoService()

    response, response_data = todo_service.get_all(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
