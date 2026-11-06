import allure
from src.services.recipe_service import RecipeService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /recipes/{id} - receita inexistente retorna 404
@allure.title('GET /recipes/999999 - status 404')
def test_get_recipes_status_404():
    folder_path = 'public-api/recipes/GET/404'
    recipe_service = RecipeService()

    response, response_data = recipe_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
