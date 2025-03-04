"""
configuration file
"""
from unittest.mock import patch, MagicMock
import json
import sqlite3
import pytest
from sqlalchemy import Integer, String, BigInteger, Date, Text, Enum, JSON, Float
from sqlalchemy.orm import scoped_session, sessionmaker

mock_env = {

        "MYSQL_USER_ID":"test",
        "MYSQL_PASSWORD":"test",
        "MYSQL_HOST":"test",
        "MYSQL_DATABASE":"test"
    }

class PatchedI(Integer):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

class PatchedB(BigInteger):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
class PatchedT(Text):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
class PatchedD(Date):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

class PatchedV(String):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

class PatchedE(Enum):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

class PatchedJ(JSON):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

class PatchedD1(Float):
    """
    class for patching to Generic data type
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

MYSQL_TYPE_MAPPINGS = {
    'INTEGER': PatchedI,
    'TINYINT': PatchedI,
    'BIGINT': PatchedB,
    'TEXT': PatchedT,
    'DATE': PatchedD,
    'VARCHAR': PatchedV,
    'ENUM': PatchedE,
    'JSON': PatchedJ,
    'DOUBLE':PatchedD1
}
POST_TYPE_MAPPINGS = {
    'JSONB': PatchedJ
}

def patch_mysql_types():
    """
    Patching mysql data types with generic types
    """
    patches = []
    for mysql_type, generic_type in MYSQL_TYPE_MAPPINGS.items():
        patcher = patch(f'sqlalchemy.dialects.mysql.{mysql_type}', generic_type)
        patches.append(patcher)
        patcher.start()
    return patches

def patch_post_types():
    """
    Patching postgres data types with generic types
    """
    patches = []
    for mysql_type, generic_type in POST_TYPE_MAPPINGS.items():
        patcher = patch(f'sqlalchemy.dialects.postgresql.{mysql_type}', generic_type)
        patches.append(patcher)
        patcher.start()
    return patches

@pytest.fixture(scope="session")
def client():
    """
    Creates the Flask test client with a mocked environment.
    """
    mock_secret_response = {
        'SecretString': json.dumps({"username": "test", "password": "test",
                                    "host": "test", "dbname": "test"})
    }
    mock_client = MagicMock()
    mock_client.get_secret_value.return_value = mock_secret_response

    with patch('boto3.session.Session.client', return_value=mock_client), \
         patch.dict('os.environ', mock_env), \
         patch.dict('sys.modules', {'flask_socketio': mock_client}):

        patch_mysql_types()
        patch_post_types()
        from tractor_config import create_app
        app = create_app()
        yield app

@pytest.fixture(scope="module")
def db_m(client):
    """
    Creates the database and tables before tests.
    """
    from tractor_config import db

    app = client
    sqlite3.connect(':memory:')
    sqlalchemy_database_uri = 'sqlite:///:memory:'

    with patch.dict(app.config, {
        'SQLALCHEMY_DATABASE_URI': sqlalchemy_database_uri,
        'SQLALCHEMY_POOL_SIZE': None,
        'SQLALCHEMY_MAX_OVERFLOW': None,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'TESTING': True
    }):
        with app.app_context():
            db.create_all()
            yield db  # Return the database instance
            db.drop_all()

@pytest.fixture(scope="function")
def db_session(db_m):
    """
    Creates a new database session for each test function.
    """
    connection = db_m.engine.connect()
    transaction = connection.begin()
    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)

    db_m.session = session  # Assign session to SQLAlchemy db instance

    yield session  # Provide the session to the test

    session.remove()
    transaction.rollback()  # Rollback after each test
    connection.close()


