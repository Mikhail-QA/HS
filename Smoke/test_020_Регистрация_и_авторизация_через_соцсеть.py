import allure
from POM.social_networks import SocialVk
from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.asserts import AssertForTest020
from POM.school_page import SchoolPage


@allure.feature("Авторизация через соцсеть")
@allure.story("Авторизоваться на сайте ДШ П через соцсеть ВК (gruzd-vikto@rambler.ru)")
class RegistrationAndAuthUserInSocialNetwork(OpenTilda):
    def test_000_reg_user(self):
        driver = self.driver
        auth_vk = SocialVk(driver)
        get_main_page = UrlHomeSchool(driver)
        open_popup_auth = TildaPage(driver)
        activity_popup = PopupSignIn(driver)
        step_assert = AssertForTest020(driver)
        with allure.step("Зайти на сайт ВК, авторизоваться П (8615883823494/Testng1991)"):
            auth_vk.auth_user_vk()
        with allure.step("Перейти на Tilda"):
            get_main_page.go_to_tilda_landing()
        with allure.step("Нажать на кнопку Начать заниматься"):
            open_popup_auth.click_button_registration()
        with allure.step("В поп-апе регистрации нажать на иконку соцсети ВК"):
            activity_popup.click_button_vk_reg()
        with allure.step("В окне Регистрации dev-passport отображается заголовок с текстом (Регистрация)"):
            self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        with allure.step("В окне Регистрации dev-passport отображается имя П (Tryavnyak Timir)"):
            self.assertEqual("Tryavnyak Timir", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        with allure.step("В окне Регистрации dev-passport отображается E-mail П (gruzd-vikto@rambler.ru)"):
            self.assertEqual("gruzd-vikto@rambler.ru",
                             driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        with allure.step("В окне Регистрации dev-passport отображается текст Вы впервые на InternetUrok.ru"):
            self.assertEqual(u"Вы впервые на InternetUrok.ru или у вас уже есть аккаунт ?",
                             driver.find_element_by_css_selector("p.center").text)
        with allure.step("В окне Регистрации dev-passport отображается кнопка (Я новый пользователь)"):
            self.assertEqual(u"Я новый пользователь", driver.find_element_by_link_text(u"Я новый пользователь").text)
        with allure.step("В окне Регистрации dev-passport отображается кнопка (У меня уже есть аккаунт)"):
            self.assertEqual(u"У меня уже есть аккаунт",
                             driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        with allure.step("В окне Регистрации dev-passport нажать на кнопку (Я новый пользователь)"):
            auth_vk.click_button_new_user()
        with allure.step("В окне Регистрации dev-passport отображается текст (Для завершения регистрации....)"):
            self.assertEqual(
                u"Для завершения регистрации введите ваш e-mail. На указанный\nвами e-mail будет отправлено письмо с ссылкой для подтверждения.",
                driver.find_element_by_css_selector("p.center").text)
        with allure.step("В окне Регистрации dev-passport отображается текст (Действующий e-mail)"):
            self.assertEqual(u"Действующий e-mail", driver.find_element_by_css_selector("label").text)
        with allure.step(
                "В окне Регистрации dev-passport в блоке Действующий e-mail отображается E-mail П (gruzd-vikto@rambler.ru)"):
            self.assertEqual("gruzd-vikto@rambler.ru", driver.find_element_by_id("user_email").get_attribute("value"))
        with allure.step("В окне Регистрации dev-passport нажать на кнопку (Зарегистрироваться)"):
            auth_vk.click_button_reg()
        with allure.step("Дождаться регистрации и убедиться появляения нотификации (Проверить почту)"):
            step_assert.check_popup_received_code()

    def test_auth_user(self):
        driver = self.driver
        get_main_page = UrlHomeSchool(driver)
        step_school = SchoolPage(driver)
        step_assert = AssertForTest020(driver)

        with allure.step("Выйти из профиля"):
            get_main_page.exit_profile()
        with allure.step("В поп-апе авторизации нажать на иконку соцсети ВК"):
            step_school.click_vk()
        with allure.step("Дождаться регистрации и убедиться появляения нотификации (Проверить почту)"):
            step_assert.check_popup_received_code()
