import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class TestOrder:

    @pytest.mark.parametrize(
        'order_button_locator, name, surname, address, metro_station, phone, delivery_date, rent_period, color, comment',
        [
            [
                MainPageLocators.TOP_ORDER_BUTTON,
                'Максат',
                'Кургамбаев',
                'Москва, улица Пушкина, дом 10',
                'Сокольники',
                '89991234567',
                '15.06.2026',
                'сутки',
                'black',
                'Позвонить за час'
            ],
            [
                MainPageLocators.BOTTOM_ORDER_BUTTON,
                'Иван',
                'Иванов',
                'Москва, улица Ленина, дом 5',
                'Черкизовская',
                '89997654321',
                '16.06.2026',
                'двое суток',
                'grey',
                'Оставить у подъезда'
            ],
        ]
    )
    def test_create_order(
            self,
            driver,
            order_button_locator,
            name,
            surname,
            address,
            metro_station,
            phone,
            delivery_date,
            rent_period,
            color,
            comment
    ):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_button(order_button_locator)

        order_page = OrderPage(driver)
        order_page.fill_first_order_form(name, surname, address, metro_station, phone)
        order_page.fill_second_order_form(delivery_date, rent_period, color, comment)

        assert order_page.check_order_success_modal_is_displayed()