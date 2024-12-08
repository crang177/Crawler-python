from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def croll_window(driver):#向下滑动滚轮会自动加载数据，所以为了获得更多数据吗，已经得到“加载更多”的按钮
    step_num=5000
    stop_num=30000
    while True:
        if stop_num-step_num<=0:
            break
            #执行js命令，命令内容可上网搜索
        driver.execute_script(f'window.scrollTo(0,{step_num})')
        step_num+=5000
        print(stop_num)
        time.sleep(0.2)


def main():
    option=webdriver.EdgeOptions()
    option.add_experimental_option("detach",True)
    driver=webdriver.Edge(options=option)
    driver.get("https://news.163.com/")


    for i in range(1,6):#为了加载更多的按钮，然后去点击
        croll_window(driver)

        #找到按钮的节点
        more_message=driver.find_element(By.XPATH,'//*[@id="index2016_wrap"]/div[3]/div[2]/div[3]/div[2]/div[5]/div/a[3]')
        #使用js来点击按钮，因为这个按钮上存在一个遮罩，直接使用click会报错
        driver.execute_script("arguments[0].click()",more_message)
        print(f'第{i}次点击')
    
    page=driver.page_source#获取到了所有的数据
    driver.quit()


if __name__=="__main__":
    main()