import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper


class VkEcosystemPageLocators:
    TITLE_LABEL = (By.XPATH, "//h1[@class='title-h2']")

class VkEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы Экосистемы ВК"):
            self.attach_screenshot()
        self.find_element(VkEcosystemPageLocators.TITLE_LABEL)