import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Дождаться видимости элемента')
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.wait_for_clickable(locator)
        self.find_element(locator).click()

    @allure.step('Заполнить поле')
    def set_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Заполнить поле и нажать Enter')
    def set_text_and_press_enter(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    @allure.step('Проскроллить к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.number_of_windows_to_be(2)
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Дождаться перехода на нужный URL')
    def wait_for_url_to_be(self, url):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Дождаться, что URL содержит нужный текст')
    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(text)
        )

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверить, что элемент отображается')
    def is_element_displayed(self, locator):
        return self.wait_for_visible(locator).is_displayed()