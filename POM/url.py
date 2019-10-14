import time

import allure


class UrlHomeSchool(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def go_to_my_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/profile/my_profile")
        assert (u"Город:", self.driver.find_element_by_css_selector(
            "div.form-group.v-space_fio:nth-child(11) label.col-sm-4.control-label").text)

    def go_to_tilda_landing(self):
        self.driver.get("https://test-school01.interneturok.ru/")
        assert (self.driver.find_element_by_css_selector(
            "div.t396__elem.tn-elem.tn-elem__596361131472555385669"))  # кнопка начать заниматься

    def exit_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/logout")

    def go_to_lesson_page_test(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/22530/video/99812")
        assert (self.driver.find_element_by_css_selector("#step9"))

    def go_to_lesson_page_1_klass(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/25029/homework/114480")
        # Математика, 1 класс , неделя 13 (25 ноября - 30 ноября)

    def go_to_lesson_page_tab_homework(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/22537/homework/99858")
        assert (self.driver.find_element_by_css_selector(
            ".next-item-btn"))
        time.sleep(2)

    def go_to_lesson_tab_test_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/22357/training_iu/98768")
        # Английский язык, 7 класс , неделя 4 (23 сентября - 28 сентября)
        assert (self.driver.find_element_by_css_selector(
            ".training-iu-section:nth-child(2) div:nth-child(1) label span.ng-binding"))
        time.sleep(1.5)

    def go_to_lesson_tab_trainer_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/22357/training_iu/98768")
        # Английский язык, 7 класс , неделя 4 (23 сентября - 28 сентября)
        assert (self.driver.find_element_by_css_selector(
            ".training-iu-section:nth-child(1) div:nth-child(1) label span.ng-binding"))
        time.sleep(1.5)

    def go_to_lesson_tab_video(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/22357/video/98763")
        # Английский язык, 7 класс , неделя 4 (23 сентября - 28 сентября)
        assert (self.driver.find_element_by_id("vlp-videobox-1"))
        time.sleep(1.5)

    def go_to_page_subjects_subscribe(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/subjects-subscribe")
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
