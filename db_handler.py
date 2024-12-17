### https://www.psycopg.org/psycopg3/docs/
import psycopg
from utils import logger_config

logger = logger_config()

def get_db_connection(db_config):
    try:
        conn = psycopg.connect(**db_config)
        return conn
    except Exception as err:
        logger.error("DB Error - {}".format(err))

def db_health(db_config):
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    try:
        query = 'SELECT "task_id" FROM "task_details" LIMIT 1;'
        cursor.execute(query,)
        # result = cur.fetchone()
        logger.info("Database healthy!")
        return {"postgres_healthy": True}
    except psycopg.Error as err:
        logger.error("Data error: {}".format(err))
        return {"postgres_healthy": False}
    finally:
        cursor.close()
        conn.close()

def get_all_tasks(db_config):
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    try:
        query = 'SELECT row_to_json(task_details) FROM "task_details";'
        cursor.execute(query,)
        return cursor.fetchall()
    except psycopg.Error as err:
        logger.error("Data error: {}".format(err))
        return {"error": 500}
    finally:
        cursor.close()
        conn.close()

def get_task_data(db_config, task_id):
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    try:
        query = 'SELECT row_to_json(task_details) FROM task_details where task_id = {};'.format(task_id)
        cursor.execute(query,)
        result = cursor.fetchone()
        if isinstance(result, tuple):
            return result
        else:
            return {"error": 404}
    except psycopg.Error as err:
        logger.error("Data error: {}".format(err))
        return {"error": 500}
    finally:
        cursor.close()
        conn.close() 

def add_new_task(db_config, task_data):
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    try:
        ### first check if task_id is unique
        result = get_task_data(db_config, task_data.task_id)
        print(result)
        if 'error' in result:
            ## no duplicate id
            query = """
                INSERT INTO task_details (task_id, task_name, task_owner, task_status)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (task_data.task_id, task_data.task_name, task_data.task_owner, task_data.task_status))
            conn.commit()
            logger.info("Record added with ID - {}".format(task_data.task_id))
            return {"task_added": True}
        return {"task_added": False, "error": 400}
    except psycopg.Error as err:
        logger.error("Data error: {}".format(err))
        return {"error": 500}
    finally:
        cursor.close()
        conn.close()