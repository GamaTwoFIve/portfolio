import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

link = 'https://www.citilink.ru/'

# Xpath конечно громоздкий но мне он нравиться, более точный так сказать
class Test_korzina(): 
    def test(self):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(15)
        noyt = browser.find_element(By.XPATH, "/html/body/div[2]/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div/a[1]").click()       
        poreaity = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[1]/div[2]/div[2]/div/button[3]/span').click() 
        time.sleep(3)       
        nout = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/a').click()                     
        vkorziny = browser.find_element(By.CLASS_NAME, 'e11w80q30.e4uhfkv0.app-catalog-1lk9ql2.e4mggex0').click()       
        namenoyt = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/div[1]/div[2]/div/div[2]/h1')
        name = namenoyt.text
        korzinaput = browser.find_element(By.CSS_SELECTOR, 'body > div.PopupScrollContainer > div > div > div > div > div.css-10n8sd6.e73syig0 > div > div > div > div.css-ass1ds.egfuobq0 > a > button').click()        
        namenoyt2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[2]/div/a/span/span')
        name2 = namenoyt2.text

        assert name == name2 

        clearkorzina = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[3]/button/span/div[2]/span').click()
        time.sleep(3)                                   
        browser.quit
        


       
        
                                                                                                                                     
         




        





        


