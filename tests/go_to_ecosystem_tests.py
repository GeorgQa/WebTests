import allure

from  core.base_test import browser
from pages.base_page import BasePageHelper
from  pages.login_page import LoginPageHelper
from  pages.vk_ecosystem_page import VkEcosystemPageHelper


BASE_URL = "https://ok.ru/"


@allure.suite("Проверка тулбара")
@allure.title("Проверка переход к проектам экосистемы VK")
def test_open_vk_ecosystem(browser):
    base_page = BasePageHelper(browser)
    base_page.get_url(BASE_URL)
    base_page.check_page()
    login_page = LoginPageHelper(browser)
    current_window_id = login_page.get_windows_id(0)
    login_page.click_vk_ecosystem()
    login_page.click_more_button()
    new_window_id = login_page.get_windows_id(1)
    login_page.switch_window(window_id=new_window_id)
    vk_ecosystem_page = VkEcosystemPageHelper(browser)
    vk_ecosystem_page.switch_window(window_id=current_window_id)
    LoginPageHelper(browser)