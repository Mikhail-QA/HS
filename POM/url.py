import time


class UrlHomeSchool(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_my_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/profile/my_profile")
        assert (
            "Моя школа:", self.driver.find_element_by_class_name("profile-courses_item_header").text)

    def go_to_tilda_landing(self):
        self.driver.get("http://iu:123456@project752209.tilda.ws/")

    def exit_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/logout")

    def go_to_lesson_page_test(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21715/video/92701")

    def go_to_lesson_page_tab_homework(self):
            self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21715/homework/92702")

    def go_to_lesson_tab_test_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18402/training_iu/91896")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)

    def go_to_lesson_tab_trainer_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18325/training_iu/90787")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)

    def go_to_lesson_tab_video(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18112/video/72658")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)

