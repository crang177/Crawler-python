from selenium import webdriver
import json
from selenium.webdriver.common.by import By
  

option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)


driver=webdriver.Edge(options=option)
driver.get("https://www.gushiwen.cn/user/login.aspx")

with open("1-12自动化工具selenium/cookies.txt","r") as fp:
    cookies=json.loads(fp.read())
print(cookies,"\n\n\n\n\n\n")

#将所有cookies合并成为一个cookies字典
for cookie in cookies :
    cookie_dict={}
    print(cookie)
    for key,value in cookie.items():
        cookie_dict[key]=value
    print(cookie_dict)
    driver.add_cookie(cookie_dict)



#刷新页面，不刷新cookies加载不进去
driver.refresh()
#点击我的
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/a[6]").click()
print(driver.save_screenshot("12自动化工具selenium/古诗文网.png"))