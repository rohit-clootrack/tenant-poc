from locust import HttpUser, task


class TenantTest(HttpUser):
    @task
    def get_tenants(self):
        self.client.get("/tenants")

    @task
    def create_tenants(self):
        payload = {"first_name": "John", "last_name": "Doe"}
        self.client.post("/tenants/", json=payload)
