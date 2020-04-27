# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        print("instantiated selenium web driver")
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_appdynamics_job(self):
        driver = self.driver
        driver.get("https://www.morganstanley.com/what-we-do/research")
        print("loaded url: https://www.morganstanley.com/what-we-do/research")

        self.assertEqual(True, self.is_element_present(By.LINK_TEXT, "Client Login"))
        driver.find_element_by_link_text("Client Login").click()
        print("clicked Client Login")

        self.assertEqual(True, self.is_element_present(By.XPATH, "//a[contains(text(),'Research Portal')]"))
        driver.find_element_by_xpath("//a[contains(text(),'Research Portal')]").click()
        print("clicked Research Portal")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print("element not found: " + what)
            self.driver.save_screenshot("ElementNotPresent.png")
            return False
        return True

    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to.alert
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.save_screenshot("FinalScreenshot.png")
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()
        print("test completed")


if __name__ == "__main__":
    unittest.main()
