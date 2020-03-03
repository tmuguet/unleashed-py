
import unleashed_py

def test_attributes(requests_mock):
    mocked_value = """{
    "Pagination": {
        "NumberOfItems": 1,
        "PageSize": 200,
        "PageNumber": 1,
        "NumberOfPages": 1
    },
    "Items": [
        {
            "Guid": "01234567-89ab-cdef-0123-456789abcdef",
            "SetName": "my-attributes",
            "Type": "Product",
            "Attributes": [
                {
                    "Guid": "23456789-abcd-ef01-2345-6789abcdef01",
                    "Name": "attribute1",
                    "Value": null,
                    "IsRequired": false
                },
                {
                    "Guid": "abcdef01-2345-6789-abcd-ef0123456789",
                    "Name": "attribute2",
                    "Value": null,
                    "IsRequired": false
                }
            ],
            "CreatedBy": "me@domain.com",
            "CreatedOn": "/Date(1583225970451)/",
            "LastModifiedBy": "me@domain.com",
            "LastModifiedOn": "/Date(1583226100532)/"
        }
    ]
}"""

    requests_mock.get('https://api.unleashedsoftware.com/AttributeSets/1', text=mocked_value)

    attributes = unleashed_py.Resource('AttributeSets', 'api-id', 'api-key', 'https://api.unleashedsoftware.com')
    assert attributes.all_results() == '[{"Guid": "01234567-89ab-cdef-0123-456789abcdef", "SetName": "my-attributes", "Type": "Product", "Attributes": [{"Guid": "23456789-abcd-ef01-2345-6789abcdef01", "Name": "attribute1", "Value": null, "IsRequired": false}, {"Guid": "abcdef01-2345-6789-abcd-ef0123456789", "Name": "attribute2", "Value": null, "IsRequired": false}], "CreatedBy": "me@domain.com", "CreatedOn": "/Date(1583225970451)/", "LastModifiedBy": "me@domain.com", "LastModifiedOn": "/Date(1583226100532)/"}]'
