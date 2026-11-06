import allure
from src.services.quote_service import QuoteService
from src.utils.validators import validate_response_with_json_schema
from src.utils.files import load_expected_data


# GET /quotes/{id} - citação única
@allure.title('GET /quotes/1 - status 200')
def test_get_quotes_single_status_200():
    folder_path = 'public-api/quotes/GET/200'
    quote_service = QuoteService()

    response, response_data = quote_service.get_id(
        1,
        expected_status=200,
        save_response_log=folder_path
    )

    expected_shape = load_expected_data(folder_path, 'b.success.single.json')
    validate_response_with_json_schema(response_data, expected_shape, validation_mode='allow-extra')
