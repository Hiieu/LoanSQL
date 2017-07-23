import os
from tempfile import mkstemp
from unittest import (
    main as ut_main,
    TestCase
)


from Loan import (
    app,
    db,
    Loan,
    Report,
    User
)


class FlaskrTestCase(TestCase):
    def init_db(self):
        """Initializes the database."""
        db.init_app(app)
        db.create_all()
        self._populate_db()
        self.db = db

    def _populate_db(self):
        """Add mocked data to database"""
        user_1 = User(name='FirstName', surname="FirstSurname")
        user_2 = User(name='SecondName', surname="SecondName")
        loan_1 = Loan(balance=56, currency='GBP')
        report_1 = Report(
            body='body1',
            loan=loan_1,
            title='TitleReport1',
            user=user_1,
        )
        report_2 = Report(user=user_2, title='TitleReport2')
        db.session.add(report_1)
        db.session.add(report_2)
        db.session.commit()

    def setUp(self):
        """Create temporary database"""
        self.db_fd, app.config['DATABASE'] = mkstemp()
        app.config.update(
            DEBUG=False,
            SQLALCHEMY_DATABASE_URI=
            'sqlite:///{0}'.format(app.config['DATABASE']),
            TESTING=True,
        )
        self.app = app.test_client()
        with app.app_context():
            self.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_user_report_relation(self):
        with app.app_context():
            # Not enought time for unit test :/
            pass

    def test_balance_validator(self):
        pass

    def test_currency_validator(self):
        pass


if __name__ == '__main__':
    ut_main()
