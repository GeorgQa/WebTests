from operator import index

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By

class BasePageLocators:
    SEARCH_FIELD= (By.XPATH, '//*[@name="st.query"]')
    BUTTON_LOGO = (By.XPATH, '//*[@data-l="t,logo"]')
    VK_ECOSYSTEM_BUTTON = (By.XPATH, "//*[@data-l='t,vk_ecosystem']")
    MORE_BUTTON = (By.XPATH, "//*[@data-l='t,more']" )

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver


    def check_page(self):
        self.find_element(BasePageLocators.BUTTON_LOGO)
        self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON)


    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, timeout=time).until(expected_conditions.visibility_of_element_located(locator=locator), message=f"Не удалось найти элемент: {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, timeout=time).until(expected_conditions.presence_of_all_elements_located(locator), message=f"Не удалось найти элементы в DOM: {locator}")

    @allure.step("Открываем страницу")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(body=self.driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

    @allure.step("Нажимаем кнопку экосистемы ВК")
    def click_vk_ecosystem(self):
        self.find_element(locator=BasePageLocators.VK_ECOSYSTEM_BUTTON).click()

    @allure.step("Нажимаем кнопку 'Ещё'")
    def click_more_button(self):
        self.find_element(locator=BasePageLocators.MORE_BUTTON).click()

    @allure.step("Присваиваем индекс конкретной старице")
    def get_windows_id(self, index):
        self.attach_screenshot()
        return self.driver.window_handles[index]

    @allure.step("Переходим на другую вкладку")
    def switch_window(self, window_id):
        self.attach_screenshot()
        self.driver.switch_to.window(window_id)
