import pymysql



#连接数据库
db=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",database="test")

#设置字符集
db.set_charset("utf8")

#创建游标对象
cursor=db.cursor()

#执行sql命令
sql="select * from user"
cursor.execute(sql)

#获取结果集（cursor.fetchall()这个是全部结果，cursor.fetchone()获取一个结果）
print(cursor.fetchall())

#受影响的行数
print(cursor.rowcount)

#添加数据时要加上
    #db.commit()相当于提交数据
    #db.rollback()在上面出错时，将数据库回滚到未添加数据时的状态
try :
    sql='insert into usser(name,age,height) values("王大锤",22,1.67)'
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


sql="select id from user"
cursor.execute(sql)

#关闭数据库连接
db.close()
