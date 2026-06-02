import allure
import pytest

from data import QUESTIONS_DATA
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Проверка текста ответа в разделе Вопросы о важном')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_answer',
        QUESTIONS_DATA
    )
    def test_question_opens_correct_answer(
            self, driver, question_locator, answer_locator, expected_answer
    ):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_question(question_locator)

        assert main_page.get_answer_text(answer_locator) == expected_answer