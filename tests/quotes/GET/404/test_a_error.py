import allure
from src.services.quote_service import QuoteService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /quotes/{id} - citação inexistente retorna 404
@allure.title('GET /quotes/999999 - status 404')
def test_get_quotes_status_404():
    folder_path = 'public-api/quotes/GET/404'
    quote_service = QuoteService()

    response, response_data = quote_service.get_id(
        999999,
        expected_status=404,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.error.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
