from gevent import monkey
monkey.patch_all()

import uuid
import random
from locust import HttpUser, task, between

class DirectUser(HttpUser):
    wait_time = between(0, 0)

    @task(4)
    def visit_homepage(self):
        url = f"/?nocache={uuid.uuid4().hex}"
        self.client.get(
            url,
            name="GET / (Homepage)",
            headers={
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
        )

    @task(1)
    def random_pages(self):
        pages = ["/about", "/contact", "/login", "/register"]
        url = f"{random.choice(pages)}?nocache={uuid.uuid4().hex}"
        self.client.get(
            url,
            name="GET / Random Pages",
            headers={
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
        )
