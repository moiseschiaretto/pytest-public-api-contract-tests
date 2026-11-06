import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /posts/{id} - post inexistente retorna 404
@allure.title('GET /posts/999999 - status 404')
def test_get_posts_status_404():
    folder_path = 'public-api/posts/GET/404'
    post_service = PostService()

    response, response_data = post_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
