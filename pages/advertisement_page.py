import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdvertisementPageLocators:
    TEXT_IN_ADVERTISEMENT = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet") and .//span[text()="Рекламный кабинет"]]')


class AdvertisementPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы рекламного кабинета"):
            self.attach_screenshot()
        self.find_element(AdvertisementPageLocators.TEXT_IN_ADVERTISEMENT)
