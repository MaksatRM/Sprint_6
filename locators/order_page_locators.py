from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница формы заказа
    NAME_FIELD = [By.XPATH, ".//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    PHONE_FIELD = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Вторая страница формы заказа
    DATE_FIELD = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    RENT_PERIOD_FIELD = [By.CLASS_NAME, 'Dropdown-placeholder']
    BLACK_COLOR_CHECKBOX = [By.ID, 'black']
    GREY_COLOR_CHECKBOX = [By.ID, 'grey']
    COMMENT_FIELD = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    # Кнопки оформления заказа
    ORDER_BUTTON = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"]
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Окно успешного заказа
    ORDER_SUCCESS_MODAL = [By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]"]
    
    @staticmethod
    def metro_station_locator(metro_station):
        return [By.XPATH, f".//div[text()='{metro_station}']"]

    @staticmethod
    def rent_period_locator(rent_period):
        return [By.XPATH, f".//div[text()='{rent_period}']"]