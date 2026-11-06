from src.config.endpoints import ENDPOINT_POSTS, ENDPOINT_POSTS_ADD, ENDPOINT_POSTS_BY_USER
from src.services.base_service import BaseService


# Serviço de posts: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class PostService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_POSTS, ENDPOINT_POSTS_ADD)

    # GET /posts/user/{userId}
    def get_by_user(self, user_id, expected_status, save_response_log=None):
        return self.send(
            method='GET',
            end_point=ENDPOINT_POSTS_BY_USER.replace('{userId}', str(user_id)),
            expected_status=expected_status,
            save_response_log=save_response_log
        )
