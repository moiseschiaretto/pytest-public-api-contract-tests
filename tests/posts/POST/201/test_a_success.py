import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# POST /posts/add - simula criação de post
@allure.title('POST /posts/add - status 201')
def test_post_posts_add_status_201():
    folder_path = 'public-api/posts/POST/201'
    body = load_json_fixture('resources/fixtures/public-api/posts/POST/request/valid.json')
    post_service = PostService()

    response, response_data = post_service.post(
        body=body,
        expected_status=201,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['title'] == body['title']
