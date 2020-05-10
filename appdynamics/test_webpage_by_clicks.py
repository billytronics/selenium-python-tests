# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        print("\n instantiated selenium web driver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_appdynamics_job(self):
        url_to_test = "https://www.amazon.com"

        driver = self.driver
        driver.get(url_to_test)
        print("loaded url: " + url_to_test)

        self.click(By.ID, "nav-link-accountList", "Account List")
        # Confirm final page is loaded by verifying below element is available:
        self.click(By.NAME, "email", "Email Address")
        print("loaded url: " + driver.current_url)

    def click(self, element_type, element_value, friendly_name):
        try:
            print("\n attempting to click: " + friendly_name)
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((element_type, element_value))).click()
            print("clicked element: " + friendly_name)
        except Exception as e:
            print(e)
            self.driver.save_screenshot("error_screenshot.png")

    def tearDown(self):
        self.driver.save_screenshot("final_screenshot.png")
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()
        print("\n -------- test completed --------")


if __name__ == "__main__":
    unittest.main()
