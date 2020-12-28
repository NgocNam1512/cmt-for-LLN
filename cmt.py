import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/namnn12/Documents/Project/cmt-for-LLN/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://www.facebook.com/mathtasyvn/photos/a.4705547702853485/4713897892018466/')
time.sleep(5) # Let the user actually see something!
driver.quit()