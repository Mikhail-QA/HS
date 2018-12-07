import unittest

import time


class AssertForTest001(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def check_text_in_tab_5(self):
        self.assertEqual(u"Класс: 1", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[1]").text)

        self.assertEqual(u"Формат обучения: «Самостоятельный»", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[2]").text)

        self.assertEqual(u"Оплата за: 1 месяц", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[3]").text)

        self.assertEqual(u"Услуга «Персональный наставник»: выключена", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[5]").text)

        self.assertEqual(u"Сумма к оплате: 800 руб.", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[2]").text)
        time.sleep(3)

    def check_text_in_demo_kassa(self):
        self.assertIn("800", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_demo_kassa_ege_hs01(self):
        self.assertIn("400", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_demo_kassa_ege_hs02(self):
        self.assertIn("6300", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"1 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nСамостоятельный",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)
        self.assertEqual(
            u"Услуга:\nПерсональный наставник\nАвтоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]").text)
        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)

    def check_text_in_widget_my_ege(self):
        self.assertEqual(
            u"Математика Профильный ЕГЭ",
            self.driver.find_element_by_css_selector(
                "#subjects-page-wrapper > div > div.col-sm-3.col-md-3 > div > div.profile-courses_item > div.profile-courses_item_list > div > div.profile-course_header.ng-binding").text)
        self.assertEqual(
            u"Тариф: Самостоятельный",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Пройдено: 0 занятий",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]").text)
        self.assertEqual(
            u"Средний балл: 0.0",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]").text)
        self.assertEqual(
            u"Автоплатеж:\nВкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]").text)

        self.assertEqual(
            u"Продлить обучение",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/button").text)


class AssertForTest002(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest002, self).__init__(driver)

    def check_text_in_tab_5(self):
        self.assertEqual(u"Класс: 7", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[1]").text)

        self.assertEqual(u"Формат обучения: «С учителем»", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[2]").text)

        self.assertEqual(u"Оплата за: 3 месяца", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[3]").text)

        self.assertEqual(u"Услуга «Персональный наставник»: включена", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[5]").text)

        self.assertEqual(u"Период действия услуги: 3 месяца", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[6]").text)

        self.assertEqual(u"Сумма к оплате: 13 800 руб.", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[2]").text)
        time.sleep(3)

    def check_text_in_demo_kassa(self):
        self.assertIn("13 800", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"7 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС учителем",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)
        self.assertEqual(
            u"Услуга:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/strong").text)

        self.assertEqual(
            u"Персональный наставник",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/a").text)

        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/div[3]").text)

        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)

    def check_text_in_widget_my_ege(self):
        self.assertEqual(
            u"Математика Профильный ЕГЭ",
            self.driver.find_element_by_css_selector(
                "#subjects-page-wrapper > div > div.col-sm-3.col-md-3 > div > div.profile-courses_item > div.profile-courses_item_list > div > div.profile-course_header.ng-binding").text)
        self.assertEqual(
            u"Тариф: Репетитор онлайн",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Пройдено: 0 занятий",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]").text)
        self.assertEqual(
            u"Средний балл: 0.0",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]").text)
        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]").text)

        self.assertEqual(
            u"Продлить обучение",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/button").text)


class AssertForTest003(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest003, self).__init__(driver)

    def check_text_in_tab_5(self):
        self.assertEqual(u"Класс: 11", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[1]").text)

        self.assertEqual(u"Формат обучения: «С зачислением»", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[2]").text)

        self.assertEqual(u"Оплата за: 9 месяцев", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[3]").text)

        self.assertEqual(u"Услуга «Персональный наставник»: включена", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[5]").text)

        self.assertEqual(u"Период действия услуги: 9 месяцев", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[6]").text)

        self.assertEqual(u"Сумма к оплате: 57 600 руб.", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[2]").text)

    def check_text_in_demo_kassa(self):
        self.assertIn("57 600", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"11 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС зачислением",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж включен",
            self.driver.find_element_by_css_selector("div.profile-course_autopay--enlistment").text)
        self.assertEqual(
            u"Услуга:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/strong").text)
        self.assertEqual(
            u"Персональный наставник",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/a").text)

        self.assertEqual(
            u"Автоплатеж:\nВкл",
            self.driver.find_element_by_css_selector(
                "div.autopay-curator").text)

        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)


class AssertForTest006(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest006, self).__init__(driver)

    def check_text_in_tab_total(self):
        self.assertEqual(u"Класс: 7 класс", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]/div[1]").text)

        self.assertEqual(u"Формат обучения: С учителем", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]/div[2]").text)

        self.assertEqual(u"Продление обучения на: 3 месяца", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]/div[3]").text)

        self.assertEqual(u"Услуга «Персональный наставник»: включена", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]/div[5]").text)

        self.assertEqual(u"Период продления услуги: 3 месяца", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]/div[6]").text)

        self.assertEqual(u"Сумма к оплате: 13 800 руб.", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[2]").text)

    def check_text_in_demo_kassa(self):
        self.assertIn("13 800", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"7 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС учителем",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)
        self.assertEqual(
            u"Услуга:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/strong").text)
        self.assertEqual(
            u"Персональный наставник",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/a").text)
        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)


class AssertForTest007(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest007, self).__init__(driver)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"7 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС учителем",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)
        self.assertEqual(
            u"Услуга:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/strong").text)
        self.assertEqual(
            u"Персональный наставник",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/a").text)
        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)


class AssertForTest008(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest008, self).__init__(driver)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"11 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС зачислением",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж включен",
            self.driver.find_element_by_css_selector("div.profile-course_autopay--enlistment").text)
        self.assertEqual(
            u"Услуга:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/strong").text)
        self.assertEqual(
            u"Персональный наставник",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/a").text)

        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_css_selector(
                "div.autopay-curator").text)

        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)


class AssertForTest009(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest009, self).__init__(driver)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"10 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС учителем",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Пробный период до:",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)

        self.assertEqual(
            u"Оплатить обучение",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/button").text)


class AssertForTest010(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest010, self).__init__(driver)

    def check_text_in_tab_5(self):
        self.assertEqual(u"Класс: 10", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[1]").text)

        self.assertEqual(u"Формат обучения: «С учителем»", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[2]").text)

        self.assertEqual(u"Оплата за: 3 месяца", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[3]").text)

        self.assertEqual(u"Услуга «Персональный наставник»: выключена", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[1]/div[5]").text)

        self.assertEqual(u"Сумма к оплате: 6 600 руб.", self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[5]/div[2]/div[2]/div[2]").text)

    def check_text_in_demo_kassa(self):
        self.assertIn("6600", self.driver.find_element_by_class_name("price__whole-amount").text)

    def check_text_in_widget_my_school(self):
        self.assertEqual(
            u"10 класс",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[1]").text)
        self.assertEqual(
            u"Формат обучения:\nС учителем",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]").text)
        self.assertEqual(
            u"Автоплатеж:\nВкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]").text)
        self.assertEqual(
            u"Услуга:\nПерсональный наставник\nАвтоплатеж:\nВыкл",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]").text)
        self.assertEqual(
            u"Продлить обучениe",
            self.driver.find_element_by_xpath(
                "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[7]").text)


class AssertForTest011(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest011, self).__init__(driver)

    def check_text_in_page_list_all_activities(self):
        self.assertEqual(u"Выбрать предметы", self.driver.find_element_by_css_selector("a.subject-switch-link").text)

        self.assertEqual(u"Список всех занятий",
                         self.driver.find_element_by_css_selector("div.schedule_header_name").text)

        self.assertEqual(u"Подробное расписание на неделю", self.driver.find_element_by_css_selector(
            "#subjects-page-wrapper > div > div > div:nth-child(3)").text)

        self.assertEqual(
            u"Алгебра. Стандартный курс Входное тестирование 03.09.2018 (неделя 2)"
            u"\nФизика. Стандартный курс Что изучает физика? Наблюдения, опыты. Гипотеза и теория 03.09.2018 (неделя 2)"
            u"\nГеометрия. Стандартный курс Геометрические фигуры. Точка, прямая, отрезок и их свойства 03.09.2018 (неделя 2)"
            u"\nФизика. Стандартный курс Входное тестирование 03.09.2018 (неделя 2)"
            u"\nГеометрия. Стандартный курс Входное тестирование 03.09.2018 (неделя 2)"
            u'\nАнглийский язык "City or country: lifestyles. Free time activities" Grammar "Present Simple or Present Continuous (revision)" 04.09.2018 (неделя 2)'
            u"\nАлгебра. Стандартный курс Выражения. Числовые выражения с переменными 04.09.2018 (неделя 2)"
            u"\nГеография Карты. Формирование рельефа Земли. Особенности рельефа Земли 05.09.2018 (неделя 2)"
            u"\nЛитература Фольклор. Предание. Былина 05.09.2018 (неделя 2)"
            u"\nРусский язык Язык как развивающееся явление. Повторение изученного о тексте, стилях и типах речи. Языковые средства, характерные для разных типов и стилей речи 05.09.2018 (неделя 2)"
            u"\nГеометрия. Эффективный курс Входное тестирование 06.09.2018 (неделя 2)"
            u"\nОбществознание Человек среди людей. Отношения между людьми 06.09.2018 (неделя 2)"
            u"\nИстория Великие географические открытия и колонизация Америки 06.09.2018 (неделя 2)"
            u"\nБиология Зоология наука о животных. Краткая история развития зоологии. Животные и окружающая среда 07.09.2018 (неделя 2)"
            u"\nИнформатика Предмет информатики. Роль информации в жизни людей 07.09.2018 (неделя 2)"
            u"\nФизика. Стандартный курс Физические величины. Единицы физических величин. Цена деления прибора 10.09.2018 (неделя 3)"
            u"\nГеометрия. Стандартный курс Луч и угол 10.09.2018 (неделя 3)"
            u"""\nАнглийский язык "Safety rules" "Word formation (adverbs from adjectives)" Grammar "Should/n't" 11.09.2018 (неделя 3)"""
            u"\nАлгебра. Стандартный курс Определение степени с натуральным показателем 11.09.2018 (неделя 3)"
            u"\nГеография Климатообразующие факторы. Климат Земли 12.09.2018 (неделя 3)"
            u"\nПоказать еще", self.driver.find_element_by_css_selector("table.schedule-list").text)


class AssertForTest012(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest012, self).__init__(driver)

    def check_text_in_page_chosen_subject(self):
        self.assertEqual(u"Домашняя школа, 11 класс:"
                         u"\n Алгебра"
                         u"\n Геометрия"
                         u"\n Информатика"
                         u"\n Физика"
                         u"\n Химия"
                         u"\n Биология"
                         u"\n Русский язык"
                         u"\n Литература"
                         u"\n Английский язык"
                         u"\n История"
                         u"\n Вводный урок"
                         u"\n Обществознание"
                         u"\n Физкультура"
                         u"\n ОБЖ"
                         u"\n Астрономия"
                         u"\n Профориентация от SuperJob"
                         u"\nДомашняя школа, 7 класс:"
                         u"\n Алгебра. Стандартный курс"
                         u"\n Геометрия. Стандартный курс"
                         u"\n Информатика"
                         u"\n Алгебра. Эффективный курс"
                         u"\n Геометрия. Эффективный курс"
                         u"\n География"
                         u"\n Физика. Стандартный курс"
                         u"\n Биология"
                         u"\n Физика. Эффективный курс"
                         u"\n Русский язык"
                         u"\n Литература"
                         u"\n Английский язык"
                         u"\n История"
                         u"\n Обществознание"
                         u"\n Физкультура"
                         u"\n Технология"
                         u"\n Профориентация от SuperJob"
                         u"\nРепетитор ЕГЭ:"
                         u"\n Математика Профильный",
                         self.driver.find_element_by_css_selector("div.block-subject-elem-container").text)


class AssertForTest013(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest013, self).__init__(driver)

    def check_popup_thanks_for_the_feedback(self):
        self.assertEqual(u"Спасибо за отзыв!", self.driver.find_element_by_css_selector(
            "body > div.modal.fade.ng-isolate-scope.iu-fade.modal-review.in > div > div > div:nth-child(4)").text)


class AssertForTest014(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest014, self).__init__(driver)

    def check_text_show_summary(self):
        self.assertEqual(u"Показать конспект", self.driver.find_element_by_css_selector(
            "#lesson-content > div > div > div > div > div:nth-child(2) > div:nth-child(3)").text)

    def check_button_hide_summary(self):
        self.assertEqual(u"Свернуть конспект", self.driver.find_element_by_css_selector("a.dotted-link").text)
        time.sleep(4)

    def check_button_display_show_next_step(self):
        self.assertEqual(u"Следующий шаг ", self.driver.find_element_by_css_selector(
            "button.btn-next-step").text)

    def check_display_show_block_ask_question(self):
        self.assertEqual(u"Задай вопрос\nВозник вопрос? Задай его учителю.\nОтправить",
                         self.driver.find_element_by_css_selector(
                             "div.shadow-block.ask-teacher-block").text)

    def check_button_go_to_schedule(self):
        self.assertEqual(u"Перейти к расписанию",
                         self.driver.find_element_by_css_selector(
                             "button.btn.btn-primary.pull-right.ng-scope").text)
        time.sleep(0.5)
        URL = "https://web-dev01.interneturok.ru/school/lesson/21829/homework/94973"
        assert self.driver.current_url == URL

    def check_message_for_ask_questions(self):
        assert (self.driver.find_element_by_css_selector("div.chat-message-content.ng-scope"))
        self.assertEqual(u"ومنظومة الظواهر الملحوظة",
                         self.driver.find_element_by_css_selector("p.msg.ng-binding").text)

    def check_file_for_ask_question(self):
        self.assertEqual(u"photo_2018-09-18_13-28-24.jpg",
                         self.driver.find_element_by_css_selector("div.msg-img.ng-scope").text)

    def check_text_successfully_download_az(self):
        self.assertEqual(u"Ваше решение успешно отправлено и ожидает проверки учителем.",
                         self.driver.find_element_by_css_selector(
                             "#lesson-content > div > div > div > div > div > div > div > div > div.fading.ng-scope.in > homework-tab-footer > div.tab-footer.tab-footer__homework.ng-scope > div > div > div.ng-scope > div > h3").text)

    def check_redirect_user_to_schedule_page(self):
        self.assertEqual(u"Выбрать предметы", self.driver.find_element_by_css_selector(
            "a.subject-switch-link").text)
        URL = "https://web-dev01.interneturok.ru/school/"
        assert self.driver.current_url == URL


class AssertForTest015(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest015, self).__init__(driver)

    def check_text_all_page(self):
        self.assertEqual(u"II четверть", self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div.col-sm-12.ng-scope > div > div > div > span").text)

    def check_url(self):
        URL = "https://web-dev01.interneturok.ru/school/student-journal/school/7"
        assert self.driver.current_url == URL


class AssertForTest016(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest016, self).__init__(driver)

    def check_text_all_page(self):
        self.assertEqual(
            u"Выбрать предметы\nЛента событий\nВсе события\nОтветы учителя\nПовторная загрузка ДЗ\nОплата\nПеренос урока\nНовая видеоконсультация\nОценка за ДЗ\nОтмененная видеоконсультация\nОтредактировано ДЗ\nКонтроль знаний\nСобытия не найдены",
            self.driver.find_element_by_css_selector(
                "div.container.ng-scope").text)

    def check_url(self):
        URL = "https://web-dev01.interneturok.ru/school/feed"
        assert self.driver.current_url == URL


class AssertForTest017(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest017, self).__init__(driver)

    def check_email_for_user(self):
        self.assertEqual(
            u"hs05@yopmail.com", self.driver.find_element_by_css_selector("label.control-label.ng-binding").text)


class AssertForTest019(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest019, self).__init__(driver)

    def check_button_name_enter(self):
        self.assertEqual(u"Войти", self.driver.find_element_by_css_selector("a.ng-isolate-scope").text)
        time.sleep(1)

    def check_url(self):
        URL = "https://web-dev01.interneturok.ru/school/login?from=logout&auth=true"
        assert self.driver.current_url == URL


class AssertForTest020(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest020, self).__init__(driver)

    def check_popup_received_code(self):
        assert (u"Получить код",
                self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div[1]/div[3]/button").text)

    def check_url(self):
        URL = "https://web-dev01.interneturok.ru/school/login?from=logout&auth=true"
        assert self.driver.current_url == URL


class AssertForTest021(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest021, self).__init__(driver)

    def check_button_finish_test(self):
        self.assertEquals(u"Повторить", self.driver.find_element_by_xpath(
            "//*[@id='lesson-content']/div/div/div/div/div/div[2]/div[2]/div/button").text)


class AssertForTest022(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest022, self).__init__(driver)

    def check_button_finish_trainer(self):
        self.assertEquals(u"Повторить", self.driver.find_element_by_xpath(
            "//*[@id='lesson-content']/div/div/div/div/div/div[2]/div[1]/div[3]/button").text)


class AssertForTest023(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest023, self).__init__(driver)

    def check_button_play_video(self):
        self.assertEquals(u"Pause", self.driver.find_element_by_xpath("//div[6]/div[3]/div/span").text)
        assert (self.driver.find_element_by_class_name("vjs-playing"))


class AssertForTest024(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest024, self).__init__(driver)

    def check_bal_and_teacher(self):
        self.assertIn("4 балла", self.driver.find_element_by_css_selector(
            "div.text-center:nth-child(7)").text)
        time.sleep(1)

    def check_bal_in_homweork_for_lesson_page(self):
        self.assertIn("Итоговая оценка: 4 / Хорошо", self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div > div > div:nth-child(2) > div").text)


class AssertForTest025(AssertForTest001):
    def __init__(self, driver):
        super(AssertForTest025, self).__init__(driver)

    def check_step_one(self):
        self.assertEqual("Доступ к материалам ограничен", self.driver.find_element_by_css_selector(
            "#lesson-content > div > div > div > div > div > div > div > div > div:nth-child(2) > div.b-empty.bl.ng-isolate-scope > div > div > div:nth-child(2)").text)

        self.assertIn(
            "Для получения доступа к заданиями со множеством вариантов условий,\nавтоматической проверкой и разными уровнями сложности\nоплатите обучение в форматах «С учителем» или «С зачислением»\nПодробнее о форматах обучения",
            self.driver.find_element_by_css_selector(
                "#lesson-content > div > div > div > div > div > div > div > div > div:nth-child(2) > div.b-empty.bl.ng-isolate-scope > div > div > div:nth-child(3)").text)

        self.assertEqual("Оплатить обучение", self.driver.find_element_by_css_selector("button.btn.btn-success").text)

    def check_step_two(self):
        self.assertIn(
            "В формате обучения «С учителем» вы сможете загрузить свое решение.\nУчитель проверит работу, даст развернутый комментарий и выставит оценку\nПодробнее",
            self.driver.find_element_by_css_selector(
                "#lesson-content > div > div > div > div > div > div > div > div > div.fading.ng-scope.in > div.tab-footer.tab-footer__homework.ng-scope").text)
