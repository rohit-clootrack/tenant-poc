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
    def get_tenants_six(self):
        headers = {"X-Tenant-Id": "six"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_seven(self):
        headers = {"X-Tenant-Id": "seven"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_eight(self):
        headers = {"X-Tenant-Id": "eight"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_nine(self):
        headers = {"X-Tenant-Id": "nine"}
        self.client.get("/tenants", headers=headers)

    @task
    def get_tenants_ten(self):
        headers = {"X-Tenant-Id": "ten"}
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

    @task
    def create_tenants_six(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "six"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_seven(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "seven"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_eight(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "eight"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_nine(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "nine"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def create_tenants_ten(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "ten"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def get_tenants_eleven(self):
        headers = {"X-Tenant-Id": "eleven"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_eleven(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "eleven"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def get_tenants_twelve(self):
        headers = {"X-Tenant-Id": "twelve"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_twelve(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "twelve"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def get_tenants_thirteen(self):
        headers = {"X-Tenant-Id": "thirteen"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_thirteen(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "thirteen"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def get_tenants_fourteen(self):
        headers = {"X-Tenant-Id": "fourteen"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_fourteen(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "fourteen"}
        self.client.post("/tenants/", json=payload, headers=headers)

    @task
    def get_tenants_fifteen(self):
        headers = {"X-Tenant-Id": "fifteen"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants_fifteen(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        headers = {"X-Tenant-Id": "fifteen"}
        self.client.post("/tenants/", json=payload, headers=headers)


"""
import requests
payload = {"first_name": "John", "last_name": "Doe"}
BASE_URL = "http://localhost:8000/api/v1.0"
headers = {"X-Tenant-Id": "one"}
response = requests.post(f"{BASE_URL}/tenants/", json=payload, headers=headers)
print(response.content)

"""
