import allure
import pytest

from pages.console_page import ConsolePage
from pages.main_page import MainPage
from services.user_service import UserService


@allure.suite("E2E")
@allure.feature("Console")
class TestConsole:
    @pytest.mark.console_1
    @allure.title("Open console page")
    def test_open_console_page(self, main_page: MainPage, console_page: ConsolePage):
        main_page.goto()
        main_page.assert_that_main_page_visible()
        main_page.header.click_on_console_link()

        console_page.assert_that_console_page_visible()

        console_page.click_on_send_rsq_button()
        console_page.response_body_container.assert_that_body_response_visible()
        console_page.response_body_container.assert_that_rsp_status_banner_visible()

        users_list, _status_code = UserService().get_list_of_user()
        response_body_text = console_page.response_body_container.get_response_body_text()
        assert users_list == response_body_text
