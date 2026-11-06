import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# PUT /todos/{id} - simula conclusão de tarefa
@allure.title('PUT /todos/1 - status 200')
def test_put_todos_status_200():
    folder_path = 'public-api/todos/PUT/200'
    body = load_json_fixture('resources/fixtures/public-api/todos/PUT/request/valid.json')
    todo_service = TodoService()

    response, response_data = todo_service.put_id(
        1,
        body=body,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['completed'] == body['completed']
