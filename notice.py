# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome(options=options)


def get_notice(url):

    driver.get(url)

    print(driver.title)

    # searchBox = driver.find_element_by_id('srchWrd')
    
    # searchBox.send_keys('전과')
    # searchBox.submit()
    # driver.find_element_by_class_name('_button fnSubmit').click()
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    html = soup.find("table", {"class": "artclTable artclHorNum1"})
    
    notice_headline = html.find('tbody').find_all("tr")
    
    notices = []
    
    for notice in notice_headline:
        n = notice.find('td', {'class': '_artclTdTitle'}).find('a')
        title = n.find('strong').string
        link = n.get('href')
        notices.append({'title': title, 'link': link})
        
    print(notices[0]['title'])
        
    driver.quit()
    
    return notices