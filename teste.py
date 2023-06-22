import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def teste():

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

driver = webdriver.Firefox()
driver.get("https://goleada.coritiba.com.br/Store")

teste()


# driver.quit();

# WebElement e = driver.findElement(By.xpath("//*[text()='Get started free']"));

# <option value="novos">mais recentes</option>