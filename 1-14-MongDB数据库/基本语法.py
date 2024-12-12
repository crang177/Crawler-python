from pymongo import MongoClient

conn=MongoClient(host="127.0.0.1",port=27017)
db=conn.study

#添加一条数据
data = db.user.insert_one({'name': '王五', 'age':30, 'sex': 'man','hpbby':"walk"})
#查看id
print(data.inserted_id)


print(db.user.find_one())
















conn.close()