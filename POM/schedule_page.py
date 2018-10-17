import time


class SchedulePage(object):
    def __init__(self, driver):
        self.driver = driver

    def select_class_10(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div/div[3]/div[10]/div/div[1]").click()
        time.sleep(1)

    def click_button_see_schedule_page(self):
        self.driver.find_element_by_css_selector("a.button").click()
        assert (self.driver.find_element_by_css_selector("a.subject-switch-link"))

    def click_button_list_all_activities(self):
        self.driver.find_element_by_link_text("Список всех занятий").click()
        assert (self.driver.find_element_by_css_selector("td.schedule-list_item_date.ng-binding"))
        time.sleep(5)

    def click_button_chosen_subject(self):
        self.driver.find_element_by_css_selector("a.subject-switch-link").click()

    def click_button_review_block(self):
        self.driver.find_element_by_css_selector("div.review-block").click()

    def written_text_in_review_block(self):
        self.driver.find_element_by_css_selector("textarea.form-control").send_keys("北京位於華北平原的西北边缘")

    def click_button_send_text_review(self):
        self.driver.find_element_by_css_selector("button.btn.btn-success.pull-right").click()
        assert (self.driver.find_element_by_css_selector(
            "body > div.modal.fade.ng-isolate-scope.iu-fade.modal-review.in > div > div > div:nth-child(4) > span"))
        time.sleep(1)

    def click_button_close_popup_feedback(self):
        self.driver.find_element_by_css_selector(
            "body > div.modal.fade.ng-isolate-scope.iu-fade.modal-review.in > div > div > div.modal-footer.modal-footer_nbt.modal-footer_mt.text-center.ng-scope > button").click()

    def go_to_lesson_page(self):
        self.driver.find_element_by_css_selector("div.schedule_list_item_info").click()
        assert (self.driver.find_element_by_css_selector("#step10"))
        time.sleep(2)

    def go_to_academic_journal(self):
        self.driver.find_element_by_css_selector("a.without-animate").click()
        assert (self.driver.find_element_by_css_selector("td.journal_table_td.ng-scope"))

    def go_to_feed(self):
        self.driver.find_element_by_css_selector("a.feed.ng-scope").click()
        assert (u"События не найдены", self.driver.find_element_by_css_selector("div.empty-block.ng-scope").text)
        # time.sleep(1)

    def click_button_my_profile(self):
        self.driver.find_element_by_css_selector("#step7 > a").click()

    def click_text_exit(self):
        self.driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

    def click_button_next_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(0.5)

    def click_button_prew_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-prevbutton ").click()
        time.sleep(0.5)

    def click_button_close_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-skipbutton").click()
        time.sleep(0.5)
