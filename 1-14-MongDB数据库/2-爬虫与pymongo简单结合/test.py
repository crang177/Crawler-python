import requests,time,os,re,pymysql
from lxml import etree
def increase_data(ls):
    
    db=pymysql.connect(host="127.0.0.1",user="root",password="123456",database="test")
    db.set_charset("utf8")
    cursor=db.cursor()
    print(cursor)

    for i in range (len(ls)):
        try :
            cursor.execute(f"insert into xigushi values({ls[i][0]},{ls[i][1]},{ls[i][2]})")
            db.commit()
            print("22")
        except:
            db.rollback()
            print("11")
    db.close()

increase_data([("1","2","3")])