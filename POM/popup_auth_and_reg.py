import time


class PopupSignIn(object):
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        self.driver.find_element_by_class_name("m-close").click()

    def go_to_popup_registration(self):
        self.driver.find_element_by_link_text("Регистрация").click()

    def go_to_popup_authorization(self):
        self.driver.find_element_by_link_text("Вход").click()

    def click_button_vk_reg(self):
        self.driver.find_element_by_xpath("//*[@id='rec59637330']/div/div/div[2]/div/div[1]/ul/li[1]/a").click()
        assert (u"Я новый пользователь",
                self.driver.find_element_by_css_selector("body > div > div.actions > a:nth-child(1)").text)

    def click_button_vk_auth(self):
        self.driver.find_element_by_xpath("//*[@id='rec59637329']/div/div/div[2]/div/div[1]/ul/li[1]/a").click()
        assert (self.driver.find_element_by_css_selector("div.header__menu.header__menu_profile"))

    def click_button_odnoklassniki(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item_icon_od").click()

    def click_button_mail(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_mm").click()

    def click_button_facebook(self):
        self.driver.find_element_by_css_selector("b-omniauth__item.b-omniauth__item_icon_fb").click()

    def click_button_google(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_gplus").click()

    def click_button_twitter(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_tw").click()

    def click_button_yandex(self):
        self.driver.find_element_by_css_selector("a.b-omniauth__item.b-omniauth__item_icon_yd").click()

    def click_button_login(self):
        self.driver.find_element_by_css_selector(
            "#form59637329 > div.t330__input-wrapper > div.t330__blockbutton > button").click()
        assert (self.driver.find_element_by_css_selector("a.dropdown-toggle"))
        time.sleep(2)

    def click_button_login_and_wait_donwload_main_page(self):
        self.driver.find_element_by_css_selector(
            "#form59637329 > div.t330__input-wrapper > div.t330__blockbutton > button").click()
        assert (self.driver.find_element_by_css_selector("div.schedule_list_item_rep_item:nth-child(1)"))
        time.sleep(10)
