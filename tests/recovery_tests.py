import allure

from  core.base_test import browser
from pages.base_page import BasePageHelper
from  pages.recovery_page import RecoveryPageHelperHelper
from  pages.login_page import LoginPageHelper

LOGIN_TEXT = "employer@gmail.com"
BASE_URL = "https://ok.ru/"
LOGIN_PASSWORD = "test1212"

@allure.suite("Проверка формы восстановления пользователя")
@allure.title("Проверка формы восстановления после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.send_login(text=LOGIN_TEXT)
    for i in range(3):
        login_page.send_password(password=LOGIN_PASSWORD)
        login_page.click_login()
    login_page.click_recovery()
    RecoveryPageHelperHelper(browser)

