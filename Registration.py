import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''customer's data'''
name = 'Mitch'
surname = 'Jankowski'
address = 'Florida Str. 123'
city = 'Tampa'
state = 'Florida'
zipcode = '33601'
ssn = '234445621'
username = 'micz'
password = 'micz123'


class ParaBankRegistration(unittest.TestCase):
    '''ParaBankRegistration class describes test case,
which concerns correct account setup by the user - registration'''

    def setUp(self):
        '''initial test conditions'''
        self.browser = webdriver.Chrome()
        self.browser.get('https://parabank.parasoft.com/parabank/index.htm')
        self.browser.maximize_window()
    

    def testCorrectRegistration(self):
        # 1. Click 'Register'
        registration = self.browser.find_element_by_xpath('//*[@id="loginPanel"]/p[2]/a')
        registration.click()
        self.browser.implicitly_wait(5)
        # 2. Enter First Name
        namefield = self.browser.find_element_by_xpath('//input[@id="customer.firstName"]')
        namefield.send_keys(name)
        # 3. Enter Last Name
        surnamefield = self.browser.find_element_by_xpath('//input[@id="customer.lastName"]')
        surnamefield.send_keys(surname)
        # 4. Provide Address
        addressfield = self.browser.find_element_by_xpath('//input[@id="customer.address.street"]')
        addressfield.send_keys(address)
        # 5. Enter City
        # 6. Enter State
        # 7. Enter Zip Code
        # 8. Skip phone number field
        # 9. Enter SSN (Social Security Number)
        # 10. Enter Username
        # 11. Enter Password
        # 12. Confirm Password
        # 13. Click 'Register'

    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
