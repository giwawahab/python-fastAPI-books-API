from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Users, Todos
from ..routers.auth import bcrypt_context
from fastapi import status

SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:giwa123%40gmail.com@localhost:5433/TestTodoApplicationDatabase"
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=StaticPool
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {
        "username": "giwa123test",
        "id": 1,
        "user_role": "admin"
    }


client = TestClient(app)

@pytest.fixture
def test_user():
    db = TestingSessionLocal()
    # Remove old test data
    db.execute( text("TRUNCATE TABLE todos, users RESTART IDENTITY CASCADE"))
    db.commit()
    user = Users(
        id=1,
        username="giwa123test",
        email="giwa123test@gmail.com",
        first_name="Wahab",
        last_name='Giwa',
        hashed_password=bcrypt_context.hash('testpassword'),
        role="admin",
        phone_number="09162233055"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    yield user
    # Cleanup
    db.execute( text("TRUNCATE TABLE todos, users RESTART IDENTITY CASCADE"))
    db.commit()
    db.close()


@pytest.fixture
def test_todo(test_user):
    db = TestingSessionLocal()
    todo = Todos(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=test_user.id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    yield todo
    db.close()