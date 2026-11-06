import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /posts - lista paginada de posts
@allure.title('GET /posts - status 200')
def test_get_posts_status_200():
    folder_path = 'public-api/posts/GET/200'
    post_service = PostService()

    response, response_data = post_service.get_all(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
