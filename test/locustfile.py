# from locust import HttpUser, task
from locust import HttpUser, task
from faker import Faker

fake = Faker()

## Generating random values
def gen_random_task_onwer():
    return fake.name()

def gen_random_task_id():
    return fake.random_int()

def gen_random_task_status():
    return fake.boolean()

def gen_random_task_name():
    return fake.job()

class GetHealthCheck(HttpUser):
    @task
    def health_check(self):
        self.client.get("/health")

    @task
    def post_task(self):
        url = "/new_task"
        payload = {
            "task_id": gen_random_task_id(),
            "task_name":  gen_random_task_name(),
            "task_owner":  gen_random_task_onwer(),
            "task_status":  gen_random_task_status()
        }
        with self.client.post(url, json=payload, catch_response=True) as response:
            # Validate response
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed: {response.text}")



# print(gen_random_task_id())
# print(gen_random_task_onwer())
# print(gen_random_task_status())
# print(gen_random_task_name())