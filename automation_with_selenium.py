from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://oblumenauense.com.br/')

searchDropdown = driver.find_element(By.XPATH, '//*[@id="tdi_37"]/div/div/div/div[2]/div/div/div/div[2]/div/a')
searchDropdown.click()

searchText = driver.find_element(By.XPATH, '//*[@id="tdi_37"]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/form/div/input')
searchText.send_keys('saude', Keys.ENTER)



