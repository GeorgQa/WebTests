import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    PASSWORD_TOGGLE_VISIBILITY_BUTTON = (By.CLASS_NAME, "vkuiFormField__iconWrapper")
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit' and (contains(@class, 'button-pro') or contains(@class, 'vkuiButton__host') or @value='Войти в Одноклассники' or .//*[text()='Войти'])]")
    LOGIN_BUTTON_WITH_QR_CODE = (By.XPATH, "//button[.//span[text() ='Войти по QR-коду']]")
    LOGIN_TAB_QR_CODE = (By.XPATH , '//*[@data-l="t,qr_tab"]')
    REGISTER_BUTTON = (By.XPATH, "//button[.//*[contains(text(), 'Зарегистрироваться')]] | //a[text()='Зарегистрироваться' and @data-l='t,register' and @tsid='login-block21_link_ffa6bf']")
    SIGN_IN_VK = ( By.XPATH, '//*[@data-l="t,vkc"]')
    SIGN_IN_MAIL_RU = ( By.XPATH, '//*[@data-l="t,mailru"]')
    SIGN_IN_YANDEX = ( By.XPATH, '//*[@data-l="t,yandex"]')
    TITLE_ERROR_ON_LOGIN = (By.XPATH , "//span[text()='Введите логин']")
    TITLE_ERROR_ON_PASSWORD = (By.XPATH , "//span[text()='Введите пароль']")
    BUTTON_RECOVER_ACCOUNT = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Восстановить'] | //button[@data-l='t,restore']")
    GO_BACK_BUTTON = (By.XPATH , "//span[text()='Отмена']")

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        try:
            self.find_element(LoginPageLocators.PASSWORD_TOGGLE_VISIBILITY_BUTTON)
            return True
        except TimeoutException:
            return False
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_WITH_QR_CODE)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.SIGN_IN_VK)
        self.find_element(LoginPageLocators.SIGN_IN_MAIL_RU)
        self.find_element(LoginPageLocators.SIGN_IN_YANDEX)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(locator=LoginPageLocators.LOGIN_BUTTON, time=2).click()

    @allure.step("Получаем текст ошибки 'Введите логин'")
    def get_error_login(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.TITLE_ERROR_ON_LOGIN).text

    @allure.step("Получаем текст ошибки 'Введите пароль'")
    def get_error_password(self):
        self.attach_screenshot()
        return  self.find_element(LoginPageLocators.TITLE_ERROR_ON_PASSWORD).text

    @allure.step("Заполняем поле логин")
    def send_login(self, text):
        self.attach_screenshot()
        return  self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)

    @allure.step("Заполняем поле пароль")
    def send_password(self, password):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.BUTTON_RECOVER_ACCOUNT).click()

    @allure.step("Нажимаем на кнопку 'Зарегистрироваться'")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(locator=LoginPageLocators.REGISTER_BUTTON, time=2).click()

