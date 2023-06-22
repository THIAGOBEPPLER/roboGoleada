import time
import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def teste(prevElem):

    while (True):

        time.sleep(1)

        elem = driver.find_element(By.ID, "ordem_busca")
        elem.click()

        #elem = driver.find_element(By.LINK_TEXT , "mais recentes")
        elem = driver.find_element(By.XPATH , "//*[text()='mais recentes']")
        elem.click()

        time.sleep(1)

        now = datetime.datetime.now()

        elem = driver.find_element(By.CLASS_NAME , "descricao_item").text
        print(elem + " " + str(now))

        time.sleep(3)
        driver.refresh()

        print(prevElem + " " + elem)


        if(prevElem != " " and prevElem != elem):
            sound()

        prevElem = elem

def sound():

    print("mudou!")


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox()
driver.get("https://goleada.coritiba.com.br/Store")




try:

    teste(" ")

except:
    
    time.sleep(60)
    teste(" ")
