from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://oblumenauense.com.br/')

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.tdb-head-search-btn')))

search_dropdown = driver.find_element(By.CSS_SELECTOR, '.tdb-head-search-btn')
search_dropdown.click()    
    
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tdb-head-search-form-input')))    

search_text = driver.find_element(By.CSS_SELECTOR, '.tdb-head-search-form-input')
search_text.send_keys('saude', Keys.ENTER)
    
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tdb-title-text')))

news_headlines = driver.find_elements(By.CSS_SELECTOR, '#tdi_76 .entry-title a')

for headline in news_headlines: 
    print('TITLE')
    print(headline.get_attribute("title"))
    print('HREF')
    print(headline.get_attribute("href"))