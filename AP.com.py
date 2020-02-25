import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import random

imie = 'Jan'
nazwisko = 'Kowalski'
a = random.randint(2,100)
b = str(a)
email = 'jan.kowalski{}@wp.pl'.format(b)

#tworze nowa klase dziedziczącą po TestCase z modułu unittest
class TestRegistration(unittest.TestCase):
    '''klasa TestRegistration opisuje przypadek testowy, który dotyczy
rejestracji konta na stronie automationpratice.com'''
        
    def setUp(self):
        '''warunki wstepne testu
            przegladarka otwarta na stronie automationpratice.com'''
        self.browser = webdriver.Chrome()
        #otwieram przegladarke Chrome
        self.browser.maximize_window()
        self.browser.get('http://automationpractice.com')
        self.browser.implicitly_wait(5)


    def testCorrectRegistration(self):
        dzien = random.randint(1,30)
        miesiac = random.randint(1,12)
        rok = random.randint(1920,2000)
        kursor = self.browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        kursor.click()
        kursor = self.browser.find_element_by_xpath('//input[@id="email_create"]')
        kursor.send_keys(email)
        kursor = self.browser.find_element_by_id('SubmitCreate')
        kursor.click()
        gender = self.browser.find_element_by_xpath('//input[@id="id_gender1"]')
        gender.click()
        fname = self.browser.find_element_by_xpath('//*[@id="customer_firstname"]')
        fname.send_keys(imie)
        lname = self.browser.find_element_by_xpath('//*[@id="customer_lastname"]')
        lname.send_keys(nazwisko)
        mail = self.browser.find_element_by_xpath('//*[@id="email"]')
        assert mail.get_attribute('value') == email
        passwd = self.browser.find_element_by_xpath('//input[@type="password"][@data-validate="isPasswd"]')
        passwd.send_keys('jankowalski')
        days = Select(self.browser.find_element_by_xpath('//select[@id="days"]'))
        days.select_by_value(str(dzien))
        months = Select(self.browser.find_element_by_xpath('//select[@id="months"]'))
        months.select_by_value(str(miesiac))
        year = Select(self.browser.find_element_by_xpath('//select[@name="years"]'))
        year.select_by_value(str(rok))
        checkbox1 = self.browser.find_element_by_xpath('//input[@type="checkbox"][@name="newsletter"]')
        checkbox1.click()
        checkbox2 = self.browser.find_element_by_xpath('//input[@type="checkbox"][@name="optin"]')
        checkbox2.click()
        adres1 = self.browser.find_element_by_xpath('//*[@id="address1"]')
        adres1.send_keys('4299 Express Lane, FL 34238 USA')
        city = self.browser.find_element_by_xpath('//input[@name="city"]')
        city.send_keys('Sarasota')
        state = Select(self.browser.find_element_by_xpath('//*[@id="id_state"]'))
        state.select_by_value('9')
        zipcode = self.browser.find_element_by_id('postcode')
        zipcode.send_keys('34238')
        phone1 = self.browser.find_element_by_xpath('//*[@id="phone"]')
        phone1.send_keys('4564005566')
        phony = self.browser.find_element_by_id('phone_mobile')
        phony.send_keys('4564005566')
        add = self.browser.find_element_by_xpath('//input[@id="alias"]')
        add.clear()
        add.send_keys('Janusz')
        register = self.browser.find_element_by_xpath('//*[@id="submitAccount"]')
        register.click()
        
            



    def tearDown(self):
        '''
        porzadki po tescie
        '''
        pass

if __name__ == '__main__':
    unittest.main()

    

