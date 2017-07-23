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


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    report = db.relationship('Report', uselist=False, back_populates='user')
    surname = db.Column(db.String(255), nullable=False)


class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column('id', db.Integer, primary_key=True)
    body = db.Column(db.Text(5242880))  # 5MB
    loan = db.relationship("Loan", back_populates="report")
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'))
    title = db.Column(db.String(255), nullable=False)
    user = db.relationship("User", back_populates="report")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Loan(db.Model):
    __tablename__ = 'loan'
    id = db.Column('id', db.Integer, primary_key=True)
    balance = db.Column(db.Integer())
    currency = db.Column(db.String(3))
    report = db.relationship("Report", back_populates="loan", uselist=False)
    __table_args__ = (
        # Validate on database level
        db.CheckConstraint(currency.in_(ALLOWED_CURRENCY)),
        db.CheckConstraint('balance >= 0')
    )


if __name__ == '__main__':
    app.run()
