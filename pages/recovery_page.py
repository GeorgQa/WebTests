import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper

class RecoveryPageLocators:
    BUTTON_PHONE = (By.XPATH, '//*[@data-l="t,phone"]')
    BUTTON_EMAIL = (By.XPATH, '//*[@data-l="t,email"]')
    QR_CODE = (By.CLASS_NAME, 'qr_code_image_wrapper')
    APPEAL_OF_SUPPORT =  (By.CLASS_NAME, "support-link_items")



class RecoveryPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.BUTTON_PHONE)
        self.find_element(RecoveryPageLocators.BUTTON_EMAIL)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.APPEAL_OF_SUPPORT)
