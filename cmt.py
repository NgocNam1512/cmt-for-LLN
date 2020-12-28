from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Đăng nhập
browser.get("https://www.facebook.com/")
sleep(random.randint(5,10))
with open("account.txt") as f:
    acc = f.readlines()
    email = acc[0].split(":")[1].replace("\n", "")
    password = acc[1].split(":")[1].replace("\n", "")

# 2a. Điền thông tin vào ô user và pass
txtUser = browser.find_element_by_id("email")
txtUser.send_keys(email) # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys(password)

# 2b. Submit form
txtPass.send_keys(Keys.ENTER)
sleep(10)

# 3. Mở URL link
browser.get("https://www.facebook.com/mathtasyvn/photos/a.4705547702853485/4713897892018466/")
sleep(random.randint(5,10))
txtComment = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
# complementary

txtComment.send_keys("Linh Linh Nguyễn #Mathtasy #Chusovathegioi")
txtComment.send_keys(Keys.ENTER)
sleep(600)
txtComment.send_keys("Linh Linh Nguyễn #Mathtasy #Chusovathegioi")
txtComment.send_keys(Keys.ENTER)
sleep(8)
# 6. Đóng browser
browser.close()