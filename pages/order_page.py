import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить имя')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнить фамилию')
    def set_surname(self, surname):
        self.set_text(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Заполнить адрес')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбрать станцию метро')
    def set_metro_station(self, metro_station):
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(OrderPageLocators.metro_station_locator(metro_station))

    @allure.step('Заполнить телефон')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить первую форму заказа')
    def fill_first_order_form(self, name, surname, address, metro_station, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Указать дату доставки')
    def set_delivery_date(self, delivery_date):
        self.set_text_and_press_enter(OrderPageLocators.DATE_FIELD, delivery_date)

    @allure.step('Выбрать срок аренды')
    def set_rent_period(self, rent_period):
        self.click_element(OrderPageLocators.RENT_PERIOD_FIELD)
        self.click_element(OrderPageLocators.rent_period_locator(rent_period))

    @allure.step('Выбрать цвет самоката')
    def choose_scooter_color(self, color):
        if color == 'black':
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

    @allure.step('Заполнить комментарий для курьера')
    def set_comment(self, comment):
        self.set_text(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку Заказать в форме заказа')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def click_yes_button(self):
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_order_form(self, delivery_date, rent_period, color, comment):
        self.set_delivery_date(delivery_date)
        self.set_rent_period(rent_period)
        self.choose_scooter_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_yes_button()

    @allure.step('Проверить, что появилось окно успешного заказа')
    def check_order_success_modal_is_displayed(self):
        return self.is_element_displayed(OrderPageLocators.ORDER_SUCCESS_MODAL)     