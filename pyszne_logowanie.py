from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class test_rejestracji(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_zakladanie_konta_valid(self):
        nazwisko = 'Kowalskit'
        email = 'tomasz.wp12@wp.pl'

        haslo = 'Czarnykotek234;'

        driver = self.driver
        driver.get('http://www.pyszne.pl/')
        time.sleep(3)
        driver.find_element_by_xpath('//button[@class="menu button-myaccount userlogin"]').click()
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="iusername"]').clear()
        driver.find_element_by_name('username').send_keys(email)
        driver.find_element_by_id('ipassword').clear()
        driver.find_element_by_id('ipassword').send_keys(haslo)
        driver.find_element_by_xpath('//*[@type="submit"][@value="Zaloguj się"]').click()


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
