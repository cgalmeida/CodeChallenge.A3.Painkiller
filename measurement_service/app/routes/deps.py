from decouple import config
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.connection import Session
# from app.usecases.user import UserUseCases

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()