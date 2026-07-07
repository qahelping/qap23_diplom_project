from playwright.sync_api import Page, expect

from core.base_page import GorestPage


class MainPage(GorestPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.root = page.locator("main")
        self.hero = self.root.locator(".hero.hero-grid")

    def assert_that_main_page_visible(self):
        expect(self.root).to_be_visible()
        expect(self.hero).to_be_visible()
