from playwright.sync_api import Page

from pages.component.header_component import HeaderComponent
from test_data.urls import BASE_URL


class GorestPage:
    def __init__(self, page):
        self.page: Page = page
        self.header = HeaderComponent(page)

    def goto(self, path: str | None = None):
        url = f"https://{BASE_URL}/{path}" if path else f"https://{BASE_URL}"
        self.page.goto(url)
