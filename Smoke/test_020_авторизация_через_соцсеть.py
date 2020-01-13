import allure
from POM.social_networks import SocialVk
from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.asserts import AssertForTest020
from POM.school_page import SchoolPage
from POM.social_networks import ExpectedResultSocial


@allure.feature("Авторизация через соцсеть")
@allure.story("Авторизоваться на сайте ДШ П через соцсеть ВК (gruzd-vikto@rambler.ru)")
class RegistrationAndAuthUserInSocialNetwork(OpenTilda):
    def test_000_aut_in_vk_user(self):
        driver = self.driver
        auth_vk = SocialVk(driver)
        get_main_page = UrlHomeSchool(driver)
        open_popup_auth = TildaPage(driver)
        activity_popup = PopupSignIn(driver)
        check = ExpectedResultSocial(driver)
        with allure.step("Зайти на сайт ВК, авторизоваться П (8615883823494/Testng1991)"):
            auth_vk.auth_user_vk()
        with allure.step("Перейти на Tilda"):
            get_main_page.go_to_tilda_landing()
        with allure.step("Нажать на кнопку Войти"):
            open_popup_auth.click_login_button()
        # with allure.step("Нажать на кнопку Начать заниматься"):
        #     open_popup_auth.click_button_registration()
        # with allure.step("В поп-апе регистрации нажать на иконку соцсети ВК"):
        #     activity_popup.click_button_vk_reg()
        # with allure.step("В окне Регистрации dev-passport отображается заголовок с текстом (Регистрация)"):
        #     self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        # with allure.step("В окне Регистрации dev-passport отображается имя П (Tryavnyak Timir)"):
        #     self.assertEqual("Tryavnyak Timir", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        # with allure.step("В окне Регистрации dev-passport отображается E-mail П (gruzd-vikto@rambler.ru)"):
        #     self.assertEqual("gruzd-vikto@rambler.ru",
        #                      driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        #
        # with allure.step("В окне Регистрации dev-passport отображается кнопка (У меня уже есть аккаунт)"):
        #     self.assertEqual(u"У меня уже есть аккаунт",
        #                      driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        # with allure.step("В окне Регистрации dev-passport нажать на кнопку (У меня уже есть аккаунт)"):
        #     auth_vk.click_button_i_have_account()
        # with allure.step(
        #         "После нажатия П редиректит на страницу авторизации (https://dev-passport.interneturok.ru/login)"):
        #     check.check_url()

    def test_auth_user(self):
        driver = self.driver
        activity_popup = PopupSignIn(driver)
        auth_vk = SocialVk(driver)
        check = ExpectedResultSocial(driver)

        with allure.step("В поп-апе авторизации нажать на иконку соцсети ВК"):
            activity_popup.click_button_vk_autorization()
        # with allure.step("В окне Регистрации dev-passport отображается заголовок с текстом (Регистрация)"):
        #     self.assertEqual(u"Регистрация", driver.find_element_by_css_selector("h3").text)
        # with allure.step("В окне Регистрации dev-passport отображается имя П (Tryavnyak Timir)"):
        #     self.assertEqual("Tryavnyak Timir", driver.find_element_by_css_selector("p.b-oauth-user__name").text)
        # with allure.step("В окне Регистрации dev-passport отображается E-mail П (gruzd-vikto@rambler.ru)"):
        #     self.assertEqual("gruzd-vikto@rambler.ru",
        #                      driver.find_element_by_css_selector("p.b-oauth-user__email").text)
        # with allure.step("В окне Регистрации dev-passport отображается кнопка (У меня уже есть аккаунт)"):
        #     self.assertEqual(u"У меня уже есть аккаунт",
        #                      driver.find_element_by_link_text(u"У меня уже есть аккаунт").text)
        # with allure.step("В окне Регистрации dev-passport нажать на кнопку (У меня уже есть аккаунт)"):
        #     auth_vk.click_button_i_have_account()
        with allure.step(
                "После нажатия П редиректит на страницу авторизации (https://dev-passport.interneturok.ru/school)"):
            check.check_url()
