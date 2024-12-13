from fastapi import FastAPI
import uvicorn
from db_handler import db_health, get_all_tasks, get_task_data
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

db_config = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": os.environ.get("DATABASE_HOST"),
    "port": 5432,
}

for item in db_config.keys():
    print(db_config[item])

@app.get("/health")
def healthCheck():
    return db_health(db_config)

@app.get("/get_tasks")
def get_tasks():
    return get_all_tasks(db_config)

@app.get('/get_task/{task_id}')
async def get_task(task_id):
    return get_task_data(db_config, task_id)

if __name__ == '__main__':
    uvicorn.run("__main__:app", port=8080, host='0.0.0.0', workers=4, reload=True)