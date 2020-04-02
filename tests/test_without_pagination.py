
import requests
import unleashed_py

def test_companies(requests_mock):
    mocked_value = """{
    "Items": [
        {
            "Guid": "01234567-89ab-cdef-0123-456789abcdef",
            "CompanyName": "MyCompany",
            "BaseCurrencyCode": "EUR",
            "DefaultTaxRate": 0
        }
    ]
}"""

    requests_mock.get('https://api.unleashedsoftware.com/Companies/1', text=mocked_value)
    requests_mock.get('https://api.unleashedsoftware.com/Companies', text=mocked_value)

    companies = unleashed_py.Resource('Companies', 'api-id', 'api-key', 'https://api.unleashedsoftware.com')
    assert companies.all_results() == '[{"Guid": "01234567-89ab-cdef-0123-456789abcdef", "CompanyName": "MyCompany", "BaseCurrencyCode": "EUR", "DefaultTaxRate": 0}]'



def test_forbidden(requests_mock):
    mocked_value = "{\"description\": \"(403) Forbidden.: The organization with Api Id 'api-key' is not found.\"}"

    requests_mock.get('https://api.unleashedsoftware.com/Companies/1', text=mocked_value, status_code=403)
    requests_mock.get('https://api.unleashedsoftware.com/Companies', text=mocked_value, status_code=403)

    try:
        companies = unleashed_py.Resource('Companies', 'api-id', 'api-key', 'https://api.unleashedsoftware.com').all_results()
        assert False
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 403
