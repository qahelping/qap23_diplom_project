from playwright.sync_api import Page
from pytest import fixture

from pages.console_page import ConsolePage
from pages.main_page import MainPage


@fixture
def main_page(page: Page):
    return MainPage(page)


@fixture
def console_page(page: Page):
    return ConsolePage(page)
