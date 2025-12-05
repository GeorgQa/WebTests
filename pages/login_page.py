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


class LoginPageLocatorsHelper(BasePage):
    pass