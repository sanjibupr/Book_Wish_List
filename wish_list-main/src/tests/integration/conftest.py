import psycopg2
import pytest
from flask_sqlalchemy import SQLAlchemy
from flaskapp.app import TestConfig, create_app
from flaskapp.extensions import db
from pytest import fixture
from sqlalchemy.sql import text

# initialize extensions below here

@pytest.fixture(scope="session")
def app():
    app = create_app(config_object=TestConfig)

    db = SQLAlchemy(app)
    file = open("./tests/integration/init_test_db.sql")
    query = text(file.read())
    db.session.execute(query)
    db.session.commit()

    with app.app_context():
        yield app
    clean_up(db)
    db.session.commit()

def clean_up(db):
    db.session.execute("DROP TABLE wl_user CASCADE")
    db.session.execute("DROP TABLE book CASCADE")
    db.session.execute("DROP TABLE wish_list CASCADE")

@pytest.fixture
def flask_client(app):

    with app.test_client(use_cookies=False) as client:
        yield client
