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
txtComment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/form/div/div/div[2]/div")

t = [300, 578, 674, 968, 1283, 1253, 1783, 1581, 783, 1023, 60, 198, 234, 119]
while True:
    temp = random.choice(t)
    print("Time to next comment:" + str(temp) +"s")
    txtComment.send_keys("Linh Linh Nguyễn #Mathtasy #Chusovathegioi")
    txtComment.send_keys(Keys.ENTER)
    sleep(temp)
    

# 6. Đóng browser
browser.close()