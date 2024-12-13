### https://www.psycopg.org/psycopg3/docs/
import psycopg
import json

def db_health(db_config):
    try:
        with psycopg.connect(**db_config) as conn:
            query = 'SELECT "task_id" FROM "task_details" LIMIT 1;'
            with conn.cursor() as cur:
                cur.execute(query,)
                result = cur.fetchone()
    except psycopg.Error as e:
        print(f"Database error: {e}")
        return {"postgres_health": False}
    return {"postgres_health": True}


def get_all_tasks(db_config):
    try:
        with psycopg.connect(**db_config) as conn:
            query = 'SELECT * FROM "task_details";'
            with conn.cursor() as cur:
                cur.execute(query,)
                return json.dumps(cur.fetchall(), ensure_ascii=False)
            
    except psycopg.Error as e:
        print(f"Database error: {e}")


def get_task_data(db_config, task_id):
    try:
        with psycopg.connect(**db_config) as conn:
            query = 'SELECT * FROM task_details where task_id = {};'.format(task_id)
            with conn.cursor() as cur:
                cur.execute(query,)
                return json.dumps(cur.fetchone(), ensure_ascii=False)
            
    except psycopg.Error as e:
        print(f"Database error: {e}")