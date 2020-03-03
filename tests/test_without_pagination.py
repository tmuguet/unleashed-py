
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
