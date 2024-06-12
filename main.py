import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class OpenCartPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get('https://demo.opencart-ru.ru/index.php?route=common/home')
        time.sleep(1.5)

    def click_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()
        time.sleep(1.5)

    def input_text(self, by, locator, text):
        element = self.driver.find_element(by, locator)
        element.send_keys(text)
        time.sleep(0.5)

    def select_option_by_value(self, by, locator, value):
        element = self.driver.find_element(by, locator)
        element.click()
        time.sleep(0.5)
        option = self.driver.find_element(By.XPATH, f"//option[@value='{value}']")
        option.click()
        time.sleep(0.5)

    def back(self):
        self.driver.back()
        time.sleep(1.5)

@pytest.fixture
def browser():
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument('--start-maximized')
    browser = webdriver.Firefox(options=firefox_option)
    yield browser
    browser.quit()

@pytest.fixture
def opencart_page(browser):
    return OpenCartPage(browser)

@allure.step("Нажать на элемент")
def step_click_element(page, by, locator):
    page.click_element(by, locator)

@allure.step("Ввести текст")
def step_input_text(page, by, locator, text):
    page.input_text(by, locator, text)

@allure.step("Выбрать опцию по значению")
def step_select_option_by_value(page, by, locator, value):
    page.select_option_by_value(by, locator, value)

@allure.step("Вернуться назад")
def step_back(page):
    page.back()

@allure.feature("Определение функционала")
@allure.story("Тестирование функции регистрации пользователя")
def test_user_registration(opencart_page):
    opencart_page.navigate_to_home_page()
    allure.attach(opencart_page.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    step_click_element(opencart_page, By.XPATH, "//a[@title='Личный кабинет']")
    step_click_element(opencart_page, By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Регистрация')]")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_email']", "chudaikinid21@st.ithub.ru")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_password']", "123456789")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_confirm_password']", "123456789")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_firstname']", "Ilya")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_lastname']", "Chudaikin")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_telephone']", "89930021561")
    step_select_option_by_value(opencart_page, By.XPATH, "//select[@id='register_country_id']", "176")
    step_select_option_by_value(opencart_page, By.XPATH, "//select[@id='register_zone_id']", "83")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_city']", "Москва")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_postcode']", "14422")
    step_input_text(opencart_page, By.XPATH, "//input[@id='register_address_1']", "ВДНХ")
    step_click_element(opencart_page, By.XPATH, "//a[@id='simpleregister_button_confirm']")

if __name__ == "__main__":
    pytest.main(args=['-s', '--alluredir', 'allure-results'])
