from flask import Flask
from flask import jsonify

from config import ma
from db_config.config import Session
from db_config.models import Transactions
from sqlalchemy import desc, extract, func

app = Flask(__name__)

ma.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/email/<client_id>")
def send_email():
    Session().query("Emails")
    return


@app.route("/<int:month>", methods=['GET'])
def get_transactions(month):
    queryTransaction = (Session().query(
        Transactions.Product_ID,
        Transactions.Quantity,
        Transactions.Price,
        Transactions.Description,
        Transactions.Date
    ).filter(extract('month', Transactions.Date) == month
    ).order_by(desc(Transactions.Quantity)).limit(3).all())

    queryTotal = Session().query(
        func.sum(Transactions.Quantity).label('TotalQuantity'),
        func.sum(Transactions.Price * Transactions.Quantity).label('TotalAmount')
    ).one()

    result_dict_list = [{
        "Total_income": float(queryTotal.TotalAmount) if queryTotal.TotalAmount is not None else None,
        "Total_quantity": int(queryTotal.TotalQuantity) if queryTotal.TotalQuantity is not None else None,
        "products": [
            {
                "Product_ID": transaction.Product_ID,
                "Quantity": transaction.Quantity,
                "Price": float(transaction.Price),
                "Description": transaction.Description
            } for transaction in queryTransaction
        ]
    }]

    return jsonify(result_dict_list)


if __name__ == '__main__':
    app.run(debug=True)