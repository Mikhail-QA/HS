import time

import allure


class PopupSignIn(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def close_popup(self):
        self.driver.find_element_by_class_name("m-close").click()

    @allure.step
    def go_to_popup_registration(self):
        self.driver.find_element_by_link_text("Регистрация").click()

    @allure.step
    def go_to_popup_authorization(self):
        self.driver.find_element_by_link_text("Вход").click()

    @allure.step
    def click_button_vk_reg(self):
        self.driver.find_element_by_xpath("//*[@id='rec59637330']/div/div/div[2]/div/div[1]/ul/li[1]/a").click()
        # self.driver.find_element_by_css_selector(
        #     "body > div.pp.pp__registration.show > div.pp__content.pp__content_registration > div.pp__content_head > div.fastlogin-box > a:nth-child(1)").click()
        assert (u"Я новый пользователь",
                self.driver.find_element_by_css_selector("body > div > div.actions > a:nth-child(1)").text)

    @allure.step
    def click_button_vk_autorization(self):
        self.driver.find_element_by_css_selector('a.auth__links-item.auth__links-item_vk').click()
        assert (self.driver.find_element_by_css_selector("a.dropdown-toggle"))

    @allure.step
    def click_button_vk_auth(self):
        self.driver.find_element_by_xpath("//*[@id='rec59637329']/div/div/div[2]/div/div[1]/ul/li[1]/a").click()
        assert (self.driver.find_element_by_css_selector("div.header__menu.header__menu_profile"))

    @allure.step
    def click_button_odnoklassniki(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item_icon_od").click()

    @allure.step
    def click_button_mail(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_mm").click()

    @allure.step
    def click_button_facebook(self):
        self.driver.find_element_by_css_selector("b-omniauth__item.b-omniauth__item_icon_fb").click()

    @allure.step
    def click_button_google(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_gplus").click()

    @allure.step
    def click_button_twitter(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_tw").click()

    @allure.step
    def click_button_yandex(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_yd").click()

    @allure.step
    def click_button_login(self):
        self.driver.find_element_by_css_selector(
            "#form59637329 > div.t330__input-wrapper > div.t330__blockbutton > button").click()
        # self.driver.find_element_by_css_selector("#singin > button").click()
        assert (self.driver.find_element_by_css_selector("a.dropdown-toggle"))
        time.sleep(2)

    @allure.step
    def click_button_login_and_wait_donwload_main_page(self):
        self.driver.find_element_by_css_selector(
            "#form59637329 > div.t330__input-wrapper > div.t330__blockbutton > button").click()
        # assert (self.driver.find_element_by_css_selector("span.green"))
        # self.driver.find_element_by_css_selector("#singin > button").click()
        assert (
            self.driver.find_element_by_css_selector("schedule-date.ng-isolate-scope"))  # первая дата в списке уроков
        time.sleep(5)
