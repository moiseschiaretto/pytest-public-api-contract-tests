import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /todos/{id} - tarefa única
@allure.title('GET /todos/1 - status 200')
def test_get_todos_single_status_200():
    folder_path = 'public-api/todos/GET/200'
    todo_service = TodoService()

    response, response_data = todo_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
