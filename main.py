#69a843b5e504ddf3e7629ba894257201
from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()


@app.get("/create_user")
def create_user( name : str ):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect( host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database=os.getenv("DB_NAME") )

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        connection.commit()
        return {"message": f"USER {name} CREATED"}
    except Exception as e:
        return {"message": f"Cant connect to database - {e}"}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
@app.get("/")
def read_root():
    return {"message": f"Hello from {os.getenv('APP_NAME')}"}
