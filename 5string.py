#和c语言有着相同的用法
print('我叫%s,今年%d岁'%('lmy',22))

#如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
str1="helloWorld"
print(str1.isalnum())   #True
str2="hello.World"
print(str2.isalnum())   #False

#返回字符串长度
print(str1.__len__())
print(len(str1))
