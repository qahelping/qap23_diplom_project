from playwright.sync_api import Page, expect


class HeaderComponent:
    def __init__(self, page: Page):
        self.root = page.locator("header")
        self.desktop = self.root.locator("nav.ml-auto")
        self.console_link = self.desktop.locator('[href="/rest-console"]')
        self.docs_link = self.desktop.locator('href="/docs"')
        ...

        self.logo = self.root.locator("div.page-shell.flex.h-16.items-center.gap-4 > a")

    def click_on_console_link(self):
        self.console_link.click()

    def click_on_docs_link(self):
        self.docs_link.click()

    def assert_that_header_visible(self):
        expect(self.root).to_be_visible()
        expect(self.desktop).to_be_visible()
        expect(self.docs_link).to_be_visible()
        expect(self.console_link).to_be_visible()
