'''
#正则表达式

#    \d匹配一个数字  \w匹配一个数字或者字母
#    *表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
#    \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格
#    \d{3}表示匹配3个数字，例如'010'
#    \d{3,8}表示3-8个数字，例如'1234567'
#     [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
#     ^表示行的开头，^\d表示必须以数字开头。
#      $表示行的结束，\d$表示必须以数字结束。

import re
test=input()
if re.match (r'^\d{3}\-\d{3,8}$',test):
    print('匹配')
else:
    print('不匹配')

'''
'''
#切分字符串
import re
s=re.split(r'[\s\,\;]+','a b ,  c ; d e   ,; f')
print(s)
'''

'''
#分组
import re
s=re.match(r'(\d{3})\-(\d{3,8})','101-123456')
print(s.group(0))
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
'''

'''
#HomeWork
import re
def is_valid_email(addr):
    if(re.match(r'^[0-9a-zA-Z]+[0-9a-zA-Z\.]*\@[0-9a-zA-Z]+\.com$',addr)):
        return True
    return  False

if __name__=="__main__":
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print('ok')
'''

'''
#HoemWork
import re
def name_of_email(addr):
    if '<' in addr:
        m1=re.match(r'^<([0-9a-zA-Z]+[0-9a-zA-Z\s]*)>([0-9a-zA-Z\s]*)\@([0-9a-zA-Z]+\.(com|org))$',addr)
        return m1.group(1)
    else:
        m2=re.match(r'([0-9a-zA-Z]+[0-9a-zA-Z\.]*)\@([0-9a-zA-Z]*\.(com|org))', addr)
        return m2.group(1)
if __name__=="__main__":
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    print('ok')
'''






