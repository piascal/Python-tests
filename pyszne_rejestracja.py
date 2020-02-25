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
        imie = 'Janusz'
        email = 'fikcyjny12@interia.pl'

        haslo = 'Czarnykotek234;'

        driver = self.driver
        driver.get('http://www.pyszne.pl/')
        time.sleep(3)
        driver.find_element_by_xpath('//button[@class="menu button-myaccount userlogin"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="userpanel-wrapper"]/section[2]/section/a[2]').click()
        time.sleep(3)
        driver.find_element_by_id('iaccountsurname').clear()
        driver.find_element_by_id('iaccountsurname').send_keys(imie)
        driver.find_element_by_id('iaccountuser').send_keys(email)
        driver.find_element_by_id('iaccountpass').send_keys(haslo)
        driver.find_element_by_id('iaccountpass2').send_keys(haslo)
        driver.find_element_by_id('registerbutton').click
        try:
            el = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/section/section[2]/p")
            print(el.text)
            assert el.text == "Dziękujemy za stworzenie swojego indywidualnego konta na Pyszne.pl. Jeszcze pozostał jeden krok do wykonania! Należy potwierdzić konto klikając na link aktywacyjny, który przesłaliśmy na adres aartys@gmail.com. Po wykonaniu tej czynności Twoje konto będzie gotowe do użytkowania."
            print('Rejestracja zkonczona powodzeniem')

        except NoSuchElementException:
            print("ERROR! Element not found")
        time.sleep(2)

        #element =

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
