from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome(options=options)
url = 'https://www.mju.ac.kr/mjukr/257/subview.do'

driver.get(url)

print(driver.title)