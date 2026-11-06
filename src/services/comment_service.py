from src.config.endpoints import ENDPOINT_COMMENTS, ENDPOINT_COMMENTS_ADD
from src.services.base_service import BaseService


# Serviço de comentários: herda post, get_all, get_id, put_id, patch_id e delete_id do BaseService
class CommentService(BaseService):
    def __init__(self):
        super().__init__(ENDPOINT_COMMENTS, ENDPOINT_COMMENTS_ADD)
