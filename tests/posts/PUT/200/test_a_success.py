import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data, load_json_fixture


# PUT /posts/{id} - simula atualização de post
@allure.title('PUT /posts/1 - status 200')
def test_put_posts_status_200():
    folder_path = 'public-api/posts/PUT/200'
    body = load_json_fixture('resources/fixtures/public-api/posts/PUT/request/valid.json')
    post_service = PostService()

    response, response_data = post_service.put_id(
        1,
        body=body,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['title'] == body['title']
