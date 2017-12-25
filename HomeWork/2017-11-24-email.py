'''
#通过QQ邮箱向网易邮箱发送了邮件
from email.mime.text import MIMEText
import smtplib
from email.header import Header
msg=MIMEText('hello,send by Python','plain','utf-8')
subject = '放假通知'
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = '1298639127@qq.com'
msg['To'] = '15358131452@163.com'
#from_addr=input("From")
#password=input('Password')
#to_addr=input('To')
#smtp_server=input('SMTP Server')
from_addr='1298639127@qq.com'
#这里需要在qq邮箱获取授权码
password='nsqzrmotwcssiaga'
to_addr='15358131452@163.com'
smtp_server='smtp.qq.com'
#这里需要使用smtplib.SMTP_SSL
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
'''

'''
#通过网易邮箱向QQ邮箱发送了邮件
from email.mime.text import MIMEText
import smtplib
from email.header import Header
msg=MIMEText('hello,send by Python','plain','utf-8')
subject = '放假通知'
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = '15358131452@163.com'
msg['To'] = '1298639127@qq.com'
#from_addr=input("From")
#password=input('Password')
#to_addr=input('To')
#smtp_server=input('SMTP Server')
from_addr='15358131452@163.com'
#使用网易邮箱的密码
password='lmy...1995'
to_addr='1298639127@qq.com'
smtp_server='smtp.163.com'
#默认端口是25
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
'''


'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#from_addr='15358131452@163.com'
#print(_format_addr('Python爱好者 <%s>' %from_addr ))

#from_addr=input("From")
#password=input('Password')
#to_addr=input('To')
#smtp_server=input('SMTP Server')
from_addr='15358131452@163.com'
#使用网易邮箱的密码
password='lmy...1995'
to_addr='1298639127@qq.com'
smtp_server='smtp.163.com'

msg=MIMEText('hello,send by Python','plain','utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#默认端口是25
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

'''


'''
#发送邮件添加附件
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr='15358131452@163.com'
password='lmy...1995'
to_addr='1298639127@qq.com'
smtp_server='smtp.163.com'

msg=MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('E:/1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#默认端口是25
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
'''

