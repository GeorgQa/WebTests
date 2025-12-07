from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    PASSWORD_TOGGLE_VISIBILITY_BUTTON = (By.CLASS_NAME, "vkuiFormField__iconWrapper")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit' and .//span[text()='Войти']]")
    LOGIN_BUTTON_WITH_QR_CODE = (By.XPATH, "//button[.//span[text() ='Войти по QR-коду']]")
    LOGIN_TAB_QR_CODE = (By.XPATH , '//*[@data-l="t,qr_tab"]')
    REGISTER_BUTTON =  (By.XPATH,"//button[@type='button' and .//span[text()='Зарегистрироваться']]")
    SIGN_IN_VK = ( By.XPATH, '//*[@data-l="t,vkc"]')
    SIGN_IN_MAIL_RU = ( By.XPATH, '//*[@data-l="t,mailru"]')
    SIGN_IN_YANDEX = ( By.XPATH, '//*[@data-l="t,yandex"]')
    TITLE_ERROR_ON_LOGIN = (By.XPATH , "//span[text()='Введите логин']")
    TITLE_ERROR_ON_PASSWORD = (By.XPATH , "//span[text()='Введите пароль']")


class LoginPageLocatorsHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_TOGGLE_VISIBILITY_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_WITH_QR_CODE)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.SIGN_IN_VK)
        self.find_element(LoginPageLocators.SIGN_IN_MAIL_RU)
        self.find_element(LoginPageLocators.SIGN_IN_YANDEX)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_login(self):
        return self.find_element(LoginPageLocators.TITLE_ERROR_ON_LOGIN).text

    def get_error_password(self):
        return  self.find_element(LoginPageLocators.TITLE_ERROR_ON_PASSWORD).text

    def send_login(self, text):
        return  self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)