import allure
from src.services.comment_service import CommentService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /comments - lista paginada de comentários
@allure.title('GET /comments - status 200')
def test_get_comments_status_200():
    folder_path = 'public-api/comments/GET/200'
    comment_service = CommentService()

    response, response_data = comment_service.get_all(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
