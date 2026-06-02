import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка успешного оформления заказа самоката')
    @pytest.mark.parametrize(
        'order_button_locator, name, surname, address, metro_station, phone, delivery_date, rent_period, color, comment',
        ORDER_DATA
    )
    def test_order_success(
            self, driver, order_button_locator, name, surname, address,
            metro_station, phone, delivery_date, rent_period, color, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.click_order_button(order_button_locator)

        order_page.fill_first_order_form(name, surname, address, metro_station, phone)
        order_page.fill_second_order_form(delivery_date, rent_period, color, comment)

        assert order_page.check_order_success_modal_is_displayed()