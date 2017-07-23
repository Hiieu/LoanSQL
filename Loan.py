from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=
    'sqlite:///Loan.db',
    SQLALCHEMY_ECHO=False,
    SECRET_KEY='A3ZZpa&Z&*kP88KhWYrf3',
    DEBUG=True,
)
db = SQLAlchemy(app)


ALLOWED_CURRENCY = ('GBP', 'USD', 'JPY')


if __name__ == '__main__':
    app.run()
