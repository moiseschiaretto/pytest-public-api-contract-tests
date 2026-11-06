import allure
from src.services.todo_service import TodoService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /todos/add - simula criação de tarefa
@allure.title('POST /todos/add - status 201')
def test_post_todos_add_status_201():
    folder_path = 'public-api/todos/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/todos/POST/request/valid.json')
    todo_service = TodoService()

    response, response_data = todo_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['todo'] == body['todo']
