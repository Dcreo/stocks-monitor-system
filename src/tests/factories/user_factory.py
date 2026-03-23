import factory
import uuid

from src.models import User

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = None

    username = factory.Faker("user_name") 
    email = factory.Faker("email")
    password = "12345678"
