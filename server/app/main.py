import time
import psycopg2
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor

from . import models
from .database import engine
from .local_env import prod_db_user, prod_db_host, prod_db_name, prod_db_pass

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host=prod_db_host,
            database=prod_db_name,
            user=prod_db_user,
            password=prod_db_pass,
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        connection_success = "Database connection was successful"
        print(connection_success)
        break
    except Exception as error:
        print("Connection to database failed")
        print(f"Error: {error}")
        time.sleep(2)
    

from .routers import cohort, student, sys_checks


@app.get("/")
async def hello_word():
    return {"msg": "Hello world"}



app.include_router(cohort.router)
app.include_router(student.router)
app.include_router(sys_checks.router)
