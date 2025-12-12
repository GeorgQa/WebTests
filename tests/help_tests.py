
import allure

from  core.base_test import browser
from pages.base_page import BasePageHelper
from pages.help_page import HelpPageHelperHelper, HelpPageLocators
from pages.advertisement_page import AdvertisementPageHelperHelper

BASE_URL = "https://ok.ru/help"

@allure.suite("Проверка формы поддержки")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    help_page = HelpPageHelperHelper(browser)
    help_page.scroll_to_element(locator=HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementPageHelperHelper(browser)



