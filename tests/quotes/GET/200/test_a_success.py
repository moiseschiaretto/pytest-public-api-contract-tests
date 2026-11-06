import allure
from src.services.quote_service import QuoteService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /quotes - lista paginada de citações
@allure.title('GET /quotes - status 200')
def test_get_quotes_status_200():
    folder_path = 'public-api/quotes/GET/200'
    quote_service = QuoteService()

    response, response_data = quote_service.get_all(
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'a.success.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
