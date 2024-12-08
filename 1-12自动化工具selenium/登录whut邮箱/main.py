from selenium import webdriver
import os,time,sys,re  
from selenium.webdriver.common.by import By


os.system("cls")
handles=[]#保存每次跳转页面的句柄
url="https://mail.whut.edu.cn/"
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
browser=webdriver.Edge(options=option)

browser.get(url=url)
handles.append(browser.window_handles[0])

id=browser.find_element(By.ID,"account_name") 
password=browser.find_element(By.ID,value="password")
btn=browser.find_element(By.ID,value="action")
id.send_keys("357128")
password.send_keys("密码")
btn.click()




#browser.window_handles[0]Webdriver的属性window_handles用来记录当前页面的句柄，当前页面的句柄为列表的第一项，所以为0
#browser.switch_to.window为Webdriver的方法switch_to.window（）移动句柄到某一个新页面
#此时的browser就到了新页面的Webdriver对象
browser.switch_to.window(browser.window_handles[0])
handles.append(browser.window_handles[0])
#Webdriver对象的current_url（）方法，用来获取此时的url，由于f‘’中是表达式，所以方法的（）不表示出来
#print(f'{browser.current_url}')



write_email_btn=browser.find_element(By.ID,"_mail_component_41_41")



write_email_btn.click()




browser.switch_to.window(browser.window_handles[0])
handles.append(browser.window_handles[0])



#主题输入
subject=browser.find_elements(By.CLASS_NAME,'nui-ipt-input')[2]
subject.send_keys("hello")

#内容输入
browser.switch_to.frame(browser.find_element(By.XPATH,'//*[@id="_mail_editor_0_432"]/div[1]/div[3]/iframe'))

