import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import CountryModel


load_dotenv()

TEST_DATABASE_URL = os.getenv("DATABASE_URL_TEST")
if not TEST_DATABASE_URL:
    raise RuntimeError("DATABASE_URL_TEST is not set. Check your .env file")

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    db.add_all([
    CountryModel(
        name="Indonesia",
        flag="🇮🇩",
        difficulty="hard",
        continent="Asia",
        similar_to=["Monaco", "Poland"],
    ),
    CountryModel(
        name="Monaco",
        flag="🇲🇨",
        difficulty="hard",
        continent="Europe",
        similar_to=["Indonesia", "Poland"],
    ),
    CountryModel(
        name="Poland",
        flag="🇵🇱",
        difficulty="medium",
        continent="Europe",
        similar_to=["Indonesia", "Monaco"],
    ),
])

    db.commit()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()