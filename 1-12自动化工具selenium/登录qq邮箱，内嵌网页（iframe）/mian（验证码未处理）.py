from selenium import webdriver 
from selenium.webdriver.common.by import By
import time,os


"""
    qq邮箱最开始的html中嵌套了一个iframe
    然后再这个iframe中又嵌套了一个iframe
    登录的表单就在后面这个iframe中,在转换到下一个iframe中只能一个一个的进入,逐级进入
"""

os.system("cls")
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Edge(options=option)
driver.get("https://mail.qq.com/")
time.sleep(1)



"""
    switch_to.frame()有三种查找iframe方式:
    进入内嵌页面后driver也就是内嵌网页的界面,原父界面的元素也就拿不到了
        1.根据索引来,也就是里面的参数直接为数字
        2.参数为属性 id 或者 name 的值,比如 driver.switch_to.frame("ptlogin_iframe"),就是根据iframe的id属性或者name属性的 值为 ptlogin_iframe 来进行查找，然后进入这个页面中
        3.参数为webelement对象(方便找到iframe的进入),即  driver.find_element(By.XPATH,'//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')

"""

"""
    返回默认界面：使用       driver.switch_to.default_content()
    返回父级 frame:使用     driver.switch_to.parent_frame()
"""




driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe'))
driver.switch_to.frame("ptlogin_iframe")



driver.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
driver.find_element(By.XPATH,'//input[@id="u"]').send_keys("账号")
driver.find_element(By.XPATH,'//input[@id="p"]').send_keys("密码")
driver.find_element(By.XPATH,'//input[@id="login_button"]').click()
