
import allure

from  core.base_test import browser
from pages.base_page import BasePage
from pages.help_page import HelpPageHelper, HelpPageLocators
from pages.advertisement_page import AdvertisementPageHelper

BASE_URL = "https://ok.ru/help"

@allure.suite("Проверка формы поддержки")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    help_page = HelpPageHelper(browser)
    help_page.scroll_to_element(locator=HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementPageHelper(browser)

