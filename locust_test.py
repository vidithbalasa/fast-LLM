from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    """
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    """

    @task
    def llm_infra(self):
        self.client.post("/v1/completions", json={
            "model": "facebook/opt-125m",
            "prompt": "San Francisco is a",
            "max_tokens": "50",
            "temperature": 0,
        })

