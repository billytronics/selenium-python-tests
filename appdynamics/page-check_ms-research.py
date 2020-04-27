# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        print("instantiated selenium web driver")
        self.driver.implicitly_wait(30)
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

    def tearDown(self):
        self.driver.save_screenshot("FinalScreenshot.png")
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()
        print("test completed")


if __name__ == "__main__":
    unittest.main()
