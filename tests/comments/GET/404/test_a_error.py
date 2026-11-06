import allure
from src.services.comment_service import CommentService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /comments/{id} - comentário inexistente retorna 404
@allure.title('GET /comments/999999 - status 404')
def test_get_comments_status_404():
    folder_path = 'public-api/comments/GET/404'
    comment_service = CommentService()

    response, response_data = comment_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
