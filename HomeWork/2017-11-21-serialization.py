'''
#序列化和反序列化
import pickle
d={'name': 'Daenerys','age':10}
with open('E:/123.txt','wb') as f:
    pickle.dump(d,f)
with open('E:/123.txt','rb') as r:
    c=pickle.load(r)
    print(c)
'''

'''
#将字典与JSON字符串转换，并写入文件json.dump() json.dumps() json.loads() json.load()
import json
d={'name': 'Daenerys','age':10}
list=[1,2,3,4,5,6,7]
with open('E:/123.txt','w') as f:
    j=json.dump(d,f)
with open('E:/123.txt','r') as r:
    text=json.load(r)
    print(text)
jsonStr='{"name": "lmy", "age": 10}'
str=json.loads(jsonStr)
print(str)
'''

#JSON与类转换
#类转换为JSON并不能直接转化，需要给它一个规则，定义一个函数，传入给default
import json
class Student():
    name=''
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'name=%s,age=%s'%(self.name,self.age)
def Stu2Json(obj):
    return {
        'name': obj.name,
        'age': obj.age,
    }
s=Student('lmy','22')
j=json.dumps(s,default=Stu2Json)
print(j)

#可以使用一种简便的方式，因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
s2=Student('lucy','22')
p=json.dumps(s2,default=lambda obj:obj.__dict__)
print(p)

#将JSON转换成类，需要定义规则，因为它并不知道类的结构是什么样的
def json2Stu(obj):
    return Student(obj['name'],obj['age'])
stu=json.loads(p,object_hook=json2Stu)
print(stu)