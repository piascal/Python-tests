import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
import time

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_logowanie(self):
        self.driver = driver
        driver.get(https://www.pyszne.pl)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
