
import unittest
import os
import sys

from datetime import datetime
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver_wait = None

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def save_screenshot(self,identier):
            prefix = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            context = self.id()
            filepath = os.getcwd()+'/Screenshots/%s_%s_%s.png'%(context,prefix,identier)
            self.driver.save_screenshot(filepath)


    def tearDown(self):
        if sys.exc_info()[0]:  # returns the info of exception being handled
            self.save_screenshot("_Failure_")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
