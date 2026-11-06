import allure
from src.services.comment_service import CommentService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /comments/{id} - comentário único
@allure.title('GET /comments/1 - status 200')
def test_get_comments_single_status_200():
    folder_path = 'public-api/comments/GET/200'
    comment_service = CommentService()

    response, response_data = comment_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
