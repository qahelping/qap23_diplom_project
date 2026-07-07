import allure
from playwright.sync_api import Page, expect

from core.base_page import GorestPage
from pages.component.response_body_component import ResponseBodyComponent


class ConsolePage(GorestPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.root = page.locator("main")
        self.send_rsq_button = self.root.locator("#rsq_send")
        self.url_input = self.root.locator("#rsq_url")
        self.method_select = self.root.locator("#rsq_type")
        self.method_select = self.root.locator("#rsq_type")
        ...
        self.response_body_container = ResponseBodyComponent(page)

    @allure.step("Click on send rsq button")
    def click_on_send_rsq_button(self):
        self.send_rsq_button.click()

    @allure.step("Assert that console page visible")
    def assert_that_console_page_visible(self):
        expect(self.root).to_be_visible()
        expect(self.send_rsq_button).to_be_visible()
        expect(self.url_input).to_be_visible()
        expect(self.method_select).to_be_visible()
