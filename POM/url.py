import time

import allure


class UrlHomeSchool(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def go_to_my_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/profile/my_profile")
        time.sleep(2)
        assert (u"E-mail:", self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[1]/div/div[1]/user-personal-info/div[7]/label").text)

    def go_to_tilda_landing(self):
        self.driver.get("https://home-school-dev01.interneturok.ru/")
        assert (self.driver.find_element_by_css_selector("a.footer__top_button.orange__link")) # кнопка начать заниматься

    def exit_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/logout")

    def go_to_lesson_page_test(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21895/video/96018")
        assert (self.driver.find_element_by_css_selector("#step9"))

    def go_to_lesson_page_1_klass(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21493/homework/91341")

    def go_to_lesson_page_tab_homework(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21895/homework/96019")
        assert (self.driver.find_element_by_css_selector(
            ".next-item-btn"))
        time.sleep(2)

    def go_to_lesson_tab_test_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18402/training_iu/91896")
        assert (self.driver.find_element_by_css_selector(
            ".training-iu-section:nth-child(2) div:nth-child(1) label span.ng-binding"))
        time.sleep(1.5)

    def go_to_lesson_tab_trainer_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18325/training_iu/90787")
        assert (self.driver.find_element_by_css_selector(
            ".training-iu-section:nth-child(1) div:nth-child(1) label span.ng-binding"))
        time.sleep(1.5)

    def go_to_lesson_tab_video(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18112/video/72658")
        assert (self.driver.find_element_by_id("vlp-videobox-1"))
        time.sleep(1.5)

    def go_to_page_subjects_subscribe(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/subjects-subscribe")
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
