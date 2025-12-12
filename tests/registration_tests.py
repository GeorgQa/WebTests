import allure

from  core.base_test import browser
from pages.base_page import BasePageHelper
from  pages.registration_page import RegistrationPageHelperHelper
from  pages.login_page import LoginPageHelper

BASE_URL = "https://ok.ru/"


@allure.suite("Проверка формы регистрации")
@allure.title("Проверка формы восстановления после нескольких неудачных попыток авторизации")
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()
    registration_page = RegistrationPageHelperHelper(browser)
    selected_country_code = registration_page.select_random_country()
    actual_country_code = registration_page.get_phone_field_value()
    assert  selected_country_code == actual_country_code , f"Полученный код страны: {selected_country_code} , не совпал с распакованным: {actual_country_code}"
