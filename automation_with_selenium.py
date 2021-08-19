from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from news import News
from datetime import datetime

try:
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get('https://oblumenauense.com.br/')

    wait = WebDriverWait(driver, 20)

    button_search_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.tdb-head-search-btn')))
    button_search_dropdown.click()    
        
    input_search_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tdb-head-search-form-input')))    
    input_search_text.send_keys('covid', Keys.ENTER)
        
    info_areas = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.tdb_loop .td-module-meta-info')))

    news_list = []

    for info_area in info_areas: 
        headline = info_area.find_element(By.CSS_SELECTOR, '.entry-title a')
        info_date = info_area.find_element(By.CSS_SELECTOR, '.entry-date')

        title = headline.get_attribute('title')
        url = headline.get_attribute('href')
        date = info_date.text #info_date.get_atribute('datetime').strftime('%x')

        news_list.append(News(title, url, date))

    url_editor = 'iraklis-dokimi'
    edit_code = 'iraklis-dokimi'

    driver.get('https://rentry.co/' + url_editor)

    button_edit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.float-left')))
    button_edit.click() 

    text_area = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.CodeMirror-code'))) 
    number_lines = len(text_area.find_elements(By.CSS_SELECTOR, '.CodeMirror-line span, CodeMirror-line span > *')) 

    for i in range(0, number_lines) :
        text_area.send_keys(Keys.SHIFT, Keys.ARROW_DOWN)

    text_area.send_keys(Keys.BACKSPACE)

    nowString = datetime.now().strftime('%d/%m/%Y - %X')
    text_area.send_keys("Atualizado em: " + nowString, Keys.ENTER)
    text_area.send_keys("Notícia | Data", Keys.ENTER)
    text_area.send_keys("------ | ------", Keys.ENTER)

    for news in news_list:
        row = "[{0}]({1}) | {2}".format(news.title, news.url, news.date)
        text_area.send_keys(row, Keys.ENTER)

    input_edit_code = driver.find_element(By.CSS_SELECTOR, '#id_edit_code')  
    input_edit_code.send_keys(edit_code)

    button_save = driver.find_element(By.CSS_SELECTOR, '#submitButton')
    button_save.click()

except Exception as e:
    print(e)
    driver.close()