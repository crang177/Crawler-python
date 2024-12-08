from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#实例化
driver=webdriver.Edge()
#访问网站
driver.get("http://www.baidu.com")
#截图
driver.save_screenshot("1-12自动化工具selenium/baidu.png")
time.sleep(3)
driver.quit()