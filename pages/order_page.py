from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        metro_locator = [By.XPATH, f".//div[text()='{metro_station}']"]
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(metro_locator)
        )
        self.driver.find_element(*metro_locator).click()

    def set_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_first_order_form(self, name, surname, address, metro_station, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone(phone)
        self.click_next_button()

    def set_delivery_date(self, delivery_date):
        date_field = self.driver.find_element(*OrderPageLocators.DATE_FIELD)
        date_field.send_keys(delivery_date)
        date_field.send_keys(Keys.ENTER)

    def set_rent_period(self, rent_period):
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_FIELD).click()
        rent_period_locator = [By.XPATH, f".//div[text()='{rent_period}']"]
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(rent_period_locator)
        )
        self.driver.find_element(*rent_period_locator).click()

    def choose_scooter_color(self, color):
        if color == 'black':
            self.driver.find_element(*OrderPageLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'grey':
            self.driver.find_element(*OrderPageLocators.GREY_COLOR_CHECKBOX).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def click_yes_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.YES_BUTTON)
        )
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def fill_second_order_form(self, delivery_date, rent_period, color, comment):
        self.set_delivery_date(delivery_date)
        self.set_rent_period(rent_period)
        self.choose_scooter_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_yes_button()

    def check_order_success_modal_is_displayed(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_MODAL)
        ).is_displayed()