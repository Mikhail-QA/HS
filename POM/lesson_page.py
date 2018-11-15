import time

import os


class LessonPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_show_summary(self):
        self.driver.find_element_by_link_text("Показать конспект").click()
        time.sleep(0.5)

    def click_button_next_step(self):
        self.driver.find_element_by_css_selector("#step9").click()
        time.sleep(1)

    def send_text_in_input_ask_question(self):
        self.driver.find_element_by_id("input-lesson-comment").send_keys("ومنظومة الظواهر الملحوظة")
        time.sleep(0.5)

    def click_button_send(self):
        self.driver.find_element_by_id("step10").click()
        time.sleep(0.5)

    def click_button_go_to_schedule(self):
        self.driver.find_element_by_css_selector("#step9 > button").click()

    def click_download_dz(self):
        self.driver.find_element_by_xpath(
            "//*[@id='lesson-content']/div/div/div/div/div/div/div/div/div[4]/homework-tab-footer/div[2]/div/div/div[2]/div/div/button").click()
        time.sleep(0.5)

    def click_button_download_file_in_ask_question(self):
        self.driver.find_element_by_css_selector("span.attach-file").click()
        time.sleep(0.5)

    def attach_img_in_upload_homework(self):
        Imagepath = os.path.abspath(
            u"D:\photo_2018-09-18_13-28-24.jpg")
        self.driver.find_element_by_id("upload-homework").clear()
        self.driver.find_element_by_id("upload-homework").send_keys(Imagepath)
        assert (u"photo_2018-09-18_13-28-24.jpg",
                self.driver.find_element_by_css_selector("div.homework-img-name.ng-binding").text)

    def attach_img_in_ask_question(self):
        Imagepath = os.path.abspath(
            u"D:\photo_2018-09-18_13-28-24.jpg")
        self.driver.find_element_by_name("attach_file_select_lesson").send_keys(Imagepath)

    def click_submit_a_job(self):
        self.driver.find_element_by_xpath(
            "//*[@id='lesson-content']/div/div/div/div/div/div/div/div/div[5]/homework-tab-footer/div[2]/div/div/div[2]/div/div/button").click()
        assert (self.driver.find_element_by_css_selector("#step9 > button"))

    def click_yes_in_popup(self):
        self.driver.find_element_by_css_selector(
            "body > div.modal.fade.ng-isolate-scope.iu-fade.submit-images.in > div > div > div.new-modal_content.ng-scope > div > button.btn.btn-success").click()
        assert (self.driver.find_element_by_css_selector("#step9 > button"))

    def click_button_next_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a.introjs-nextbutton").click()
        time.sleep(1)

    def click_button_prew_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-prevbutton").click()
        time.sleep(0.5)

    def click_button_close_in_tour(self):
        self.driver.find_element_by_css_selector("a.introjs-skipbutton").click()

    def go_test(self):
        self.driver.find_element_by_css_selector(
            "#lesson-content > div > div > div > div > div > div.training-iu-table.b-practice > div.training-iu-section.tests > div > button").click()

    def go_trainer(self):
        self.driver.find_element_by_css_selector(
            "#lesson-content > div > div > div > div > div > div.training-iu-table.b-practice > div.training-iu-section.trainers > div:nth-child(3) > button").click()

    def click_play_video_iu(self):
        self.driver.find_element_by_id("vlp-videobox-1").click()
        time.sleep(2)
