from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:giwa123%40gmail.com@localhost:5433/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = 'postgresql://neondb_owner:npg_bgALrld0n5jE@ep-crimson-frost-awd3o2g1-pooler.c-12.us-east-1.aws.neon.tech/todo_app_db?sslmode=require&channel_binding=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()