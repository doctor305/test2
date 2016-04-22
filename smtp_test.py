# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time
import os

mailto_list=['94644276@qq.com']           #收件人(列表)
mail_host="smtp.tom.com"            #使用的邮箱的smtp服务器地址
mail_user="smtp2016"                           #用户名
mail_pass="jinfeng305"                             #密码
mail_postfix="tom.com"                     #邮箱的后缀
print u'请输入发送的邮箱地址（格式如 123@qq.com）：'
mailto_list.append(raw_input())

def get_path():
    if os.path.isfile('C:\Program Files\Tencent\QQ\QQLicense.rtf'):
        return 'C:\Program Files\Tencent\QQ\QQLicense.rtf'
    elif os.path.isfile('D:\Program Files\Tencent\QQ\QQLicense.rtf'):
        return 'D:\Program Files\Tencent\QQ\QQLicense.rtf'
    else:
        return 'C:\Windows\PFRO.log'
def send_mail(to_list,sub,content):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    
    me="python test"+"<"+mail_user+"@"+mail_postfix+">"
    
##    msg = MIMEText(content,_subtype='plain')
    
    msg = MIMEText(open(get_path(),'rb').read(),'base64','utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    msg['Content-Type']='application/octet-stream'
    msg['Content-Disposition']='attachment;filename="log.rtf"'
    msgRoot.attach(msg)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
for i in range(5):
    if send_mail(mailto_list,"hello","haha!"):  #邮件主题和邮件内容
        print "done!"
        break
    else:
        print "failed!"
    time.sleep(1)
    
