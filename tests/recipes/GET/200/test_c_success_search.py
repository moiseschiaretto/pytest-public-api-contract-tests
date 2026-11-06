import allure
from src.services.recipe_service import RecipeService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /recipes/search?q= - busca por termo
@allure.title('GET /recipes/search - status 200')
def test_get_recipes_search_status_200():
    folder_path = 'public-api/recipes/GET/200'
    recipe_service = RecipeService()

    response, response_data = recipe_service.get_search(
        'chicken',
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'c.success.search.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
