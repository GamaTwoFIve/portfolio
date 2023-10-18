import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.citilink.ru/catalog/noutbuki/'
# заход на сайт, сортировка по рейтингу, добавление товара в корзину,очистка корзины
# Xpath конечно громоздкий но мне он нравиться, более точный так сказать
class Test_korzina(): 
    def test(self):
        browser = webdriver.Chrome()
        browser.get(link)
        
        

        po_retingy = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/div[2]/div[2]/div/button[3]")))
        po_retingy.click()
        
        vsplivai_okno = browser.find_element(By.XPATH, "//button[text()='OK']").click()

        noytbyk_v_korziny =browser.find_element(By.XPATH, "//button//span[text()='В корзину']")
        noytbyk_v_korziny.click()
        time.sleep(3)
        zpomnim_nazvanie_noytbyka = browser.find_element(By.XPATH, "//div[@class='css-hdphih e1xk8xnt0']")
        nazvanie = zpomnim_nazvanie_noytbyka.text

        perehod_v_korziny = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Перейти в корзину']"))).click()


        noyt_v_korzine =  WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']//span")))
        nazvanie_nuyta_v_karzine = noyt_v_korzine.text
        assert nazvanie == nazvanie_nuyta_v_karzine
        
        ochistit_korziny =  WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Очистить корзину']"))).click()
        
        
                                          
        browser.quit
        



                                                                                      
         




        





        


