
import unleashed_py

def test_stockonhandwarehouses(requests_mock):
    mocked_value = """{
  "Items": [
    {
      "WarehouseId": "23456789-abcd-ef01-2345-6789abcdef01",
      "Warehouse": "Warehouse 1",
      "AvailableQty": 518
    },
    {
      "WarehouseId": "abcdef01-2345-6789-abcd-ef0123456789",
      "Warehouse": "Warehouse 2",
      "AvailableQty": 0
    }
  ]
}"""

    requests_mock.get('https://api.unleashedsoftware.com/StockOnHand/12345678-9abc-def0-1234-56789abcdef0/AllWarehouses', text=mocked_value)

    item = unleashed_py.ItemDetail('StockOnHand', '12345678-9abc-def0-1234-56789abcdef0', 'AllWarehouses', 'api-id', 'api-key', 'https://api.unleashedsoftware.com')
    assert item.all_results() == '[{"WarehouseId": "23456789-abcd-ef01-2345-6789abcdef01", "Warehouse": "Warehouse 1", "AvailableQty": 518}, {"WarehouseId": "abcdef01-2345-6789-abcd-ef0123456789", "Warehouse": "Warehouse 2", "AvailableQty": 0}]'
