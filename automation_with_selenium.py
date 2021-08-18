from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
#driver.maximize_window()

driver.get('https://oblumenauense.com.br/')

searchDropdown = driver.find_element(By.XPATH, '//*[@id="tdi_37"]/div/div/div/div[2]/div/div/div/div[2]/div/a')
searchDropdown.click()
    
    
searchText = driver.find_element(By.XPATH, '//*[@id="tdi_37"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/form/div/input')
searchText.send_keys('saude', Keys.ENTER)
    
titulos_noticias = driver.find_elements(By.CSS_SELECTOR, '#tdi_76 .entry-title a')

for titulo in titulos_noticias: 
    print('Tag Name!')
    print(titulo.tag_name)
    print('TITLE')
    print(titulo.get_attribute("title"))
    print('HREF')
    print(titulo.get_attribute("href"))
    print('ELEMENTO')
    print(titulo)




