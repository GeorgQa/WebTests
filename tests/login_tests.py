import allure

from  core.base_test import browser
from pages.base_page import BasePageHelper
from  pages.login_page import LoginPageHelper

BASE_URL = "https://ok.ru/"
ERROR_LOGIN ="Введите логин"
ERROR_PASSWORD = "Введите пароль"
TEST_DATA_TEXT_LOGIN = "employer@gmail.com"

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert  login_page.get_error_login() == ERROR_LOGIN

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустом поле пароля в форме авторизации")
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.send_login(TEST_DATA_TEXT_LOGIN)
    login_page.click_login()
    assert login_page.get_error_password() == ERROR_PASSWORD