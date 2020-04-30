# -*- coding: utf-8 -*-
import unittest

import requests


class AppDynamicsJob(unittest.TestCase):

    def test_appdynamics_job(self):
        api_to_test = "http://httpbin.org/get"

        print("\n attempting to reach api: " + api_to_test)
        r = requests.get(api_to_test)
        print("\n received response code: " + str(r.status_code))
        print("\n response json: \n" + r.text)

        # Confirm response is successful:
        self.assertEqual(200, r.status_code)
        print("\n asserting response status code = 200")
        print("** response confirmed as expected **")

    def tearDown(self):
        print("\n -------- test completed --------")


if __name__ == "__main__":
    unittest.main()
