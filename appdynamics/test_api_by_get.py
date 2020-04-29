# -*- coding: utf-8 -*-
import unittest

import requests


class AppDynamicsJob(unittest.TestCase):

    def test_appdynamics_job(self):
        api_to_test = "http://httpbin.org/get"

        print("attempting to reach api: " + api_to_test)
        r = requests.get(api_to_test)
        print("received response code: " + str(r.status_code))
        print("response json: " + r.text)

        # Confirm response is successful:
        self.assertEqual(200, r.status_code)
        print("response confirmed as expected")

    def tearDown(self):
        print("test completed")


if __name__ == "__main__":
    unittest.main()
