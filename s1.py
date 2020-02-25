from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU')
cena = browser.find_element_by_xpath('//*[contains(text(), "18.89")]')
print(cena.text)
