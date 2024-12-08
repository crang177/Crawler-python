from selenium import webdriver
import ddddocr,time
from selenium.webdriver.common.by import By

#不自动关闭浏览器的方法
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)


driver=webdriver.Edge(options=option)
driver.get("https://www.gushiwen.cn/")
time.sleep(1)
mine=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/a[6]")
mine.click()
  


username=driver.find_element(By.ID,"email")
password=driver.find_element(By.ID,"pwd")



username.send_keys("账号")
password.send_keys('密码')



#element对对象可以有一个专门截图的方法：screenshot（）
driver.find_element(By.ID,"imgCode").screenshot('1-12自动化工具selenium/yzm.png')
ocr=ddddocr.DdddOcr(show_ad=False)
with open('1-12自动化工具selenium/yzm.png','rb') as f:
    bytes=f.read()
yzm=ocr.classification(bytes)



yzm_input=driver.find_element(By.ID,"code")
yzm_input.send_keys(yzm.upper())


login_button=driver.find_element(By.ID,"denglu")
login_button.submit() #看类型是submit，提交表单