import allure
from POM.social_networks import SocialVk
from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.social_networks import ExpectedResultSocial


@allure.feature("Авторизация через соцсеть")
@allure.story("Авторизоваться на сайте ДШ П через соцсеть ВК (gruzd-vikto@rambler.ru)")
class RegistrationAndAuthUserInSocialNetwork(OpenTilda):
    def test_000_aut_in_vk_user(self):
        driver = self.driver
        auth_vk = SocialVk(driver)
        get_main_page = UrlHomeSchool(driver)
        open_popup_auth = TildaPage(driver)
        # Зайти на сайт ВК, авторизоваться П (8615883823494/Testng1991)"):
        auth_vk.auth_user_vk()
        get_main_page.go_to_tilda_landing()
        open_popup_auth.click_login_button()

    def test_auth_user(self):
        driver = self.driver
        activity_popup = PopupSignIn(driver)
        check = ExpectedResultSocial(driver)

        activity_popup.click_button_vk_autorization()
        check.check_url()
