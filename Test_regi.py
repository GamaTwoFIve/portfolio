import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
link = "http://suninjuly.github.io/simple_form_find_task.html"

# заполнить обязательные поля регистрации и нажать кнопку подтвердить за 3 секунды 
class Test_registr():

    def test(self, browser):

        
        browser.get(link)
        


        fistname = browser.find_element(By.NAME, 'first_name')
        fistname.send_keys('Kostya')
        
        lastname = browser.find_element(By.NAME, 'last_name')
        lastname.send_keys('Gyrenkov')
        
        city = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
        city.send_keys('Saint Petersburg')
        
        country = browser.find_element(By.ID, 'country')
        country.send_keys('Russian federation')
        
        button = browser.find_element(By.ID, 'submit_button').click()

        

