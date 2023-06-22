import time
import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from playsound import playsound

def teste(prevElem):

    while (True):

        time.sleep(5)

        elem = driver.find_element(By.ID, "ordem_busca")
        elem.click()

        #elem = driver.find_element(By.LINK_TEXT , "mais recentes")
        elem = driver.find_element(By.XPATH , "//*[text()='mais recentes']")
        elem.click()
        elem.click()

        time.sleep(5)

        now = datetime.datetime.now()

        elem = driver.find_element(By.CLASS_NAME , "descricao_item").text
        print(elem + " " + str(now))

        time.sleep(5)
        driver.refresh()

        print(prevElem + " " + elem)


        if(prevElem != " " and prevElem != elem):
            playSound()

        prevElem = elem

def playSound():

    print("Change!")

    for x in range(5):
        print("Alarm!")
        playsound('alarm.wav')

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
