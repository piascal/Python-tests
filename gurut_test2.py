from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class gurutest2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def testing(self):
        browser = self.driver
        browser.get('http://www.demo.guru99.com/V4/')
        browser.maximize_window()
        uid = browser.find_element_by_xpath('//input[@type="text"][@name="uid"]')
        uid.send_keys('mngr238822')
        pwd = browser.find_element_by_xpath('//input[@type="password"]')
        pwd.send_keys('YtAhYva')
        lgn = browser.find_element_by_xpath('//input[@type="submit"]')
        lgn.click()


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
