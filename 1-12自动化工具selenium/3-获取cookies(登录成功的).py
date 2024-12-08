from selenium import webdriver
import ddddocr,time,json
from selenium.webdriver.common.by import By

#不自动关闭浏览器的方法
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Edge(options=option)
driver.get("https://www.gushiwen.cn/")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/a[6]").click()

driver.find_element(By.ID,"email").send_keys("18008567665")
password=driver.find_element(By.ID,"pwd").send_keys('a123456')

#element对对象可以有一个专门截图的方法：screenshot（）
driver.find_element(By.ID,"imgCode").screenshot('1-12自动化工具selenium/yzm.png')

ocr=ddddocr.DdddOcr(show_ad=False)
with open('1-12自动化工具selenium/yzm.png','rb') as f:
    bytes=f.read()
yzm=ocr.classification(bytes)

driver.find_element(By.ID,"code").send_keys(yzm.upper())
login_button=driver.find_element(By.ID,"denglu").submit() #看类型是submit，提交表单

cookies=driver.get_cookies()
with open("1-12自动化工具selenium/cookies.txt",'w') as fp:
    fp.write(json.dumps(cookies,indent=4))


