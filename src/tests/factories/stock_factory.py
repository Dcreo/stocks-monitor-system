import factory
import uuid

from src.models import Stock

class StockFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Stock
        sqlalchemy_session = None

    name = factory.Faker("name") 
    price = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    ticker = factory.LazyFunction(lambda: f"Ticker_{uuid.uuid4()}")
    exchange = "Moex"
