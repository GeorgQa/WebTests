import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper
import random


class RegistrationPageLocators:
    COUNTRY_ITEM =(By.XPATH, "//*[@class='country-select_i']")
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    SUPPORT_COLL_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')



class RegistrationPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_COLL_BUTTON)

    def select_random_country(self):
        random_number = random.randint(a=0,b=212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute(name="text")
        country_items[random_number].click()
        return country_code

    def get_phone_field_value(self):
        with allure.step("Проверяем корректность выбора случайной страны и сравниваем"):
            self.attach_screenshot()
        return  self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute(name="value")




