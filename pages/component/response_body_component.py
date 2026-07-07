import json

import allure
from playwright.sync_api import Page, expect

from core.logger import logger
from models.user_models import UsersResponse


class ResponseBodyComponent:
    def __init__(self, page: Page):
        self.root = page.locator('[data-tabs-initial="body"]').nth(-1)
        self.tab_bar = self.root.locator('[data-tabs-initial="body"] .tab-bar')
        self.code_shell_body = self.root.locator(".code-shell.is-active .code-shell-body")
        self.response_body_text = self.root.locator("#rsp_body")
        ...
        self.rsp_status_banner = self.root.locator("#rsp_status_banner")

    @allure.step("Get text from response body container")
    def get_response_body_text(self):
        text = self.response_body_text.all_text_contents()
        logger.info("[response_body_text] %s", text)

        text_parsed = json.loads(text[0])
        return UsersResponse(users=text_parsed)

    def assert_that_rsp_status_banner_visible(self):
        expect(self.rsp_status_banner).to_be_visible()

    def assert_that_body_response_visible(self):
        expect(self.root).to_be_visible()
        expect(self.code_shell_body).to_be_visible()
