import allure
from src.services.comment_service import CommentService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /comments/add - simula criação de comentário
@allure.title('POST /comments/add - status 201')
def test_post_comments_add_status_201():
    folder_path = 'public-api/comments/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/comments/POST/request/valid.json')
    comment_service = CommentService()

    response, response_data = comment_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['body'] == body['body']
