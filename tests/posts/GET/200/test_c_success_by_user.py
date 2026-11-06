import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /posts/user/{userId} - posts de um usuário
@allure.title('GET /posts/user/5 - status 200')
def test_get_posts_by_user_status_200():
    folder_path = 'public-api/posts/GET/200'
    post_service = PostService()

    response, response_data = post_service.get_by_user(
        5,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'c.success.by-user.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
