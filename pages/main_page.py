import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import MAIN_URL, DZEN_URL


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(MAIN_URL)

    @allure.step('Кликнуть по вопросу')
    def click_question(self, question_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Кликнуть по кнопке Заказать')
    def click_order_button(self, order_button_locator):
        self.scroll_to_element(order_button_locator)
        self.click_element(order_button_locator)

    @allure.step('Кликнуть по логотипу Самокат')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекс')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        super().switch_to_new_window()

    @allure.step('Дождаться загрузки главной страницы')
    def wait_for_main_page_url(self):
        self.wait_for_url_to_be(MAIN_URL)

    @allure.step('Дождаться открытия Дзен')
    def wait_for_dzen_url(self):
        self.wait_for_url_contains(DZEN_URL)