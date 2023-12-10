from config import ma
from db_config.models import Transactions


class transaction_schema(ma.SQLAutoAlchemySchema):
    class Meta:
        model = Transactions
