import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class gurutest1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testing(self):
        browser = self.driver
        browser.get('http://www.demo.guru99.com/V4/')
        browser.maximize_window()
        userID = browser.find_element_by_name('uid')
        userID.send_keys('mngr238822')
        pswd = browser.find_element_by_name('password')
        pswd.send_keys('YtAhYva')
        logn = browser.find_element_by_xpath('//*[contains(@type,"sub")]')
        logn.click()





    def tearDown(self):
        time.sleep(15)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    
