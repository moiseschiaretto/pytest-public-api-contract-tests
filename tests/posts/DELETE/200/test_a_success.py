import allure
from src.services.post_service import PostService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# DELETE /posts/{id} - simula exclusão de post
@allure.title('DELETE /posts/1 - status 200')
def test_delete_posts_status_200():
    folder_path = 'public-api/posts/DELETE/200'
    post_service = PostService()

    response, response_data = post_service.delete_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')

    assert response_data['isDeleted'] is True
