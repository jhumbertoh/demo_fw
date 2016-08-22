from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():
    '''
    common page elements
    '''

    def __init__(self,driver, driver_wait = 10):
        self.driver = driver
        self.driver_wait = driver_wait

    def get_title(self):
        return self.driver.title
