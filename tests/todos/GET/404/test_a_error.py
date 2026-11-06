import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /todos/{id} - tarefa inexistente retorna 404
@allure.title('GET /todos/999999 - status 404')
def test_get_todos_status_404():
    folder_path = 'public-api/todos/GET/404'
    todo_service = TodoService()

    response, response_data = todo_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
