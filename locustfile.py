from locust import HttpUser, task


class TenantTest(HttpUser):
    @task
    def get_tenants(self):
        headers = {"X-Tenant-Id": "rohit.localhost"}
        self.client.get("/tenants", headers=headers)

    @task
    def create_tenants(self):
        headers = {"X-Tenant-Id": "rohit.localhost"}
        payload = {"first_name": "John", "last_name": "Doe"}
        self.client.post("/tenants/", json=payload, headers=headers)
