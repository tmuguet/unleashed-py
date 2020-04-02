
import requests
import unleashed_py

def test_stockonhand(requests_mock):
    mocked_value = """{
    "ProductCode": "CODE",
    "ProductDescription": "Product Description",
    "ProductGuid": "12345678-9abc-def0-1234-56789abcdef0",
    "ProductSourceId": null,
    "ProductGroupName": "MyProductGroup",
    "WarehouseId": "",
    "Warehouse": "",
    "WarehouseCode": "",
    "DaysSinceLastSale": 0,
    "OnPurchase": 42,
    "AllocatedQty": 0,
    "AvailableQty": 56,
    "QtyOnHand": 56,
    "AvgCost": 1337.42,
    "TotalCost": 654325.245,
    "Guid": "12345678-9abc-def0-1234-56789abcdef0",
    "LastModifiedOn": "/Date(1583240449473)/"
}"""

    requests_mock.get('https://api.unleashedsoftware.com/StockOnHand/12345678-9abc-def0-1234-56789abcdef0', text=mocked_value)

    item = unleashed_py.Item('StockOnHand', '12345678-9abc-def0-1234-56789abcdef0', 'api-id', 'api-key', 'https://api.unleashedsoftware.com')
    assert item.result() == '{"ProductCode": "CODE", "ProductDescription": "Product Description", "ProductGuid": "12345678-9abc-def0-1234-56789abcdef0", "ProductSourceId": null, "ProductGroupName": "MyProductGroup", "WarehouseId": "", "Warehouse": "", "WarehouseCode": "", "DaysSinceLastSale": 0, "OnPurchase": 42, "AllocatedQty": 0, "AvailableQty": 56, "QtyOnHand": 56, "AvgCost": 1337.42, "TotalCost": 654325.245, "Guid": "12345678-9abc-def0-1234-56789abcdef0", "LastModifiedOn": "/Date(1583240449473)/"}'


def test_forbidden(requests_mock):
    mocked_value = "{\"description\": \"(403) Forbidden.: The organization with Api Id 'api-key' is not found.\"}"

    requests_mock.get('https://api.unleashedsoftware.com/StockOnHand/12345678-9abc-def0-1234-56789abcdef0', text=mocked_value, status_code=403)

    try:
        item = unleashed_py.Item('StockOnHand', '12345678-9abc-def0-1234-56789abcdef0', 'api-id', 'api-key', 'https://api.unleashedsoftware.com').result()
        assert False
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 403
