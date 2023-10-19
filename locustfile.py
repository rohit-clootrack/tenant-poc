from locust import HttpUser, task


class TenantTest(HttpUser):
    @task
    def get_tenants_one(self):
        headers = {"X-Tenant-Id": "one"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_two(self):
        headers = {"X-Tenant-Id": "two"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_three(self):
        headers = {"X-Tenant-Id": "three"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_four(self):
        headers = {"X-Tenant-Id": "four"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_five(self):
        headers = {"X-Tenant-Id": "five"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_one(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "one"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_two(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "two"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_three(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "three"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_four(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "four"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_five(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "five"}
        self.client.post("/tenants/", json=payload, headers=headers)


"""
import requests
payload = {"first_name": "John", "last_name": "Doe"}
BASE_URL = "http://localhost:8000/api/v1.0"
headers = {"X-Tenant-Id": "one"}
response = requests.post(f"{BASE_URL}/tenants/", json=payload, headers=headers)
print(response.content)

"""
