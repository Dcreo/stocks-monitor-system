from src.models import Stock
from src.tests.utils.model_asserts import assert_model_fields

def test_stock_model():
    assert_model_fields(Stock, [
        "id", "name", "ticker", "price", "exchange"
    ])

# def test_stock_create(db):
#     stock = Stock(
#         name="TestCompany",
#         ticker="CompanyTicker",
#         exchange="Exchange",
#     )
#
#     db.add(stock)
#     db.commit()
#     db.refresh(stock)
#
#     assert stock.id is not None
