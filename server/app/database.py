from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .local_env import prod_db_user, prod_db_host, prod_db_name, prod_db_pass


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{prod_db_user}:{prod_db_pass}@{prod_db_host}/{prod_db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()
