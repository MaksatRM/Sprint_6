from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestLogo:

    def test_click_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_order_button(MainPageLocators.TOP_ORDER_BUTTON)
        main_page.click_scooter_logo()
        main_page.wait_for_main_page_url()

        assert driver.current_url == MainPage.URL

    def test_click_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_dzen_url()

        assert 'dzen.ru' in driver.current_url