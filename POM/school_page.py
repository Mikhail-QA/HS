import time
from selenium.webdriver import ActionChains


class SchoolPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element_class_name("a.logo").click()

    def click_the_feedback(self):
        self.driver.find_element_class_name("div.review-block").click()

    def hover_mouse_to_button_my_profile(self):
        element_to_hover_over = self.driver.find_element_by_css_selector("#step7 > a")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)

    def click_button_exit_in_tab_my_profile(self):
        self.driver.find_element_by_css_selector("#step7 > ul > li:nth-child(9) > a").click()

    def go_to_popup_registration(self):
        self.driver.find_element_by_class_name("page-login-footer__text").click()
        assert (self.driver.find_element_by_css_selector("button.form-button"))

    def go_to_popup_authorization(self):
        self.driver.find_element_by_link_text("Авторизуйтесь").click()

    def click_vk(self):
        self.driver.find_element_by_css_selector("a.page-loign-social-list__link.vk-login").click()
        assert (u"Проверить почту",
                self.driver.find_element_by_css_selector("a.btn.btn-success.btn-success__ok").text)


class LandingPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_to_start(self):
        self.driver.find_element_by_css_selector("span.btn-wrap-summer").click()

    def click_sign_up(self):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > input").click()
        assert (self.driver.find_element_by_css_selector("div.new-modal__body"))
        time.sleep(2)


class FormSignIn(SchoolPage):
    def __init__(self, driver):
        super(FormSignIn, self).__init__(driver)

    def click_button_login(self):
        self.driver.find_element_by_css_selector("#page-login > div > iu-authorization > div > form > button").click()
        time.sleep(4)
        assert (self.driver.find_elements_by_css_selector("div.header__menu.header__menu_profile"))
        time.sleep(1)

    def click_button_login_teacher(self):
        self.driver.find_element_by_css_selector("#page-login > div > iu-authorization > div > form > button").click()
        time.sleep(4)
        assert (self.driver.find_elements_by_css_selector(
            "div.filter:nth-child(2) span:nth-child(2)"))
        time.sleep(1)

    def click_button_login_admin(self):
        self.driver.find_element_by_css_selector("#page-login > div > iu-authorization > div > form > button").click()
        time.sleep(4)
        assert (self.driver.find_elements_by_css_selector(".btn"))
        time.sleep(1)


class FormRegistration(SchoolPage):
    def __init__(self, driver):
        super(FormRegistration, self).__init__(driver)

    def click_sign_up(self):
        self.driver.find_element_by_css_selector(
            "#page-login > div > iu-registration > div > form > button").click()
        assert (self.driver.find_element_by_css_selector("div.new-modal_header"))
