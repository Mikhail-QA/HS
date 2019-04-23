import allure
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs01
from POM.asserts import AssertForTest025
from POM.url import UrlHomeSchool


@allure.feature("Тариф Самостоятельный")
@allure.story("Проверка отсутствия загрузки ДЗ и заглушка на Яклассе")
class LoginAndGoToLessonPageCheckHomeworkAndYaklass(OpenTilda):
    def test_000_go_lesson_page(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs01(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs01@yopmail.com/123456"):
            step_user.enter_email(user_name="hs01@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()

    def test_001_failing_download_homework(self):
        driver = self.driver
        go_lesson_page = UrlHomeSchool(driver)
        step_assert = AssertForTest025(driver)
        with allure.step(
                "Перейти на страницу урока Математика, 1 класс , неделя 13 (19 ноября - 24 ноября)Задача (условие, вопрос)."):
            go_lesson_page.go_to_lesson_page_1_klass()
        with allure.step("В шаге № 1 Якласса отображается заглушка с текстом Доступ к материалам ограничен"):
            step_assert.check_step_one()
        with allure.step(
                "В шаге №2 отображается заглушка В формате обучения «С учителем» вы сможете загрузить свое решение."):
            step_assert.check_step_two()
