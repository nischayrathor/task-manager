from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
import uvicorn
from db_handler import db_health, get_all_tasks, get_task_data, add_new_task
import os

app = FastAPI()

class NewTask(BaseModel):
    task_id: int
    task_name: str
    task_owner: str
    task_status: bool

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

DB_CONFIG = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": os.environ.get("DATABASE_HOST"),
    "port": 5432,
    "sslmode": os.environ.get("SSLMODE"),
}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Task Manager App</title>
        </head>
        <body>
            <h1>Welcome to Task Manager app!</h1>
        </body>
    </html>
    """

@app.get("/health")
async def healthCheck():
    result = db_health(DB_CONFIG)
    if result['postgres_healthy']:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content=result, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/get_tasks")
async def get_tasks():
    result = get_all_tasks(DB_CONFIG)
    if 'error' in result:
        return JSONResponse(content=result, status_code=result['error'])
    else:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@app.get('/get_task/{task_id}')
async def get_task(task_id):
    result = get_task_data(DB_CONFIG, task_id)
    if 'error' in result:
        return JSONResponse(content=result, status_code=result['error'])
    else:
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@app.post('/new_task')
async def new_task(task_data: NewTask):
    result = add_new_task(DB_CONFIG, task_data)
    if result['task_added']:
        return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content=result, status_code=result['error'])

if __name__ == '__main__':
    uvicorn.run("__main__:app", headers=[("server", "awesome-server")], port=8080, host='0.0.0.0', workers=4, reload=True)