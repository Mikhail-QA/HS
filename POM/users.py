import allure
import time


class Hs01(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs01@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(2) > input").send_keys(
            password)

    def enter_email(self, user_name="hs01@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)

    def reg_mobile(self, number="+71234567"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(3) > input").send_keys(
            number)


class Hs02(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs02@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(2) > input").send_keys(
            password)

    def enter_email(self, user_name="hs02@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)

        # self.driver.find_element_by_name("user[password]").send_keys(password)

    def reg_mobile(self, number="+712345678"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(3) > input").send_keys(
            number)


class Hs03(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs03@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(2) > input").send_keys(
            password)

    def enter_email(self, user_name="hs03@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)

    def reg_mobile(self, number="+7123456789"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(3) > input").send_keys(
            number)


class Hs04(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs04@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(2) > input").send_keys(
            password)

    def reg_mobile(self, number="+7123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(3) > input").send_keys(
            number)

    def enter_email(self, user_name="hs04@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)


class Hs05(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs05@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(2) > input").send_keys(
            password)

    @allure.step
    def enter_email(self, user_name="hs05@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    @allure.step
    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)

    def reg_mobile(self, number="+71234567890"):
        self.driver.find_element_by_css_selector(
            "#iuAuthContainer > div > div.auth__modal__body > div > div:nth-child(3) > form:nth-child(9) > div:nth-child(3) > input").send_keys(
            number)


class Hs06(object):
    def __init__(self, driver):
        self.driver = driver

    def reg_email(self, user_name="hs06@yopmail.com"):
        self.driver.find_element_by_css_selector(
            "#page-login > div > iu-registration > div > form > div:nth-child(1) > input").send_keys(
            user_name)

    def reg_password(self, password="123456"):
        self.driver.find_element_by_css_selector(
            "#page-login > div > iu-registration > div > form > div:nth-child(2) > input").send_keys(
            password)

    def enter_email(self, user_name="hs06@yopmail.com"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[1]/input").send_keys(user_name)

        # self.driver.find_element_by_name("user[email]").send_keys(user_name)

    def enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//*[@id='singin']/div[2]/input").send_keys(password)
        time.sleep(1)


class Teacher(object):
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, user_name="teacher-test"):
        self.driver.find_element_by_name("email").send_keys(user_name)

    def enter_password(self, password="teacher-test"):
        self.driver.find_element_by_name("password").send_keys(password)


class Admin(object):
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, user_name="school.interneturok@yandex.ru"):
        self.driver.find_element_by_name("email").send_keys(user_name)

    def enter_password(self, password="34t3hEOfbTT2k"):
        self.driver.find_element_by_name("password").send_keys(password)


class IuUseryopmail(object):

    def __init__(self, driver):
        self.driver = driver

    def reg_enter_email(self, user_name="iuuser@yopmail.com"):
        self.driver.find_element_by_xpath("//div/label[1]/input").send_keys(user_name)

    def reg_enter_password(self, password="123456"):
        self.driver.find_element_by_xpath("//div/label[2]/input").send_keys(password)
