from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators

class MainPage:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get(self.URL)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, question_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(question_locator)
        )
        self.driver.find_element(*question_locator).click()

    def get_answer_text(self, answer_locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(answer_locator)
        ).text
    def click_order_button(self, order_button_locator):
        self.scroll_to_element(order_button_locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(order_button_locator)
        )
        self.driver.find_element(*order_button_locator).click()
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        )
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.number_of_windows_to_be(2)
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_main_page_url(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(self.URL)
        )

    def wait_for_dzen_url(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains('dzen.ru')
        )