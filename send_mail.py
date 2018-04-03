#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
'''
import smtplib  
from email.mime.text import MIMEText  
import os
import socket, fcntl, struct


mailto_list=["hopeaktian@foxmail.com", "napeaktian@163.com"] 
mail_host="smtp.sohu.com"  #设置服务器
mail_user="hopeaktian"    #用户名
mail_pass="tf1998225"   #口令 
mail_postfix="sohu.com"  #发件箱的后缀

def get_ip(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])  

def send_mail(to_list,sub,content):  
    me="hopeaktian"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content, 'plain', 'utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔  
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

if __name__ == '__main__':
    myip=get_ip("ens33")
    print myip
    mes="你好，树莓派刚刚开机了，IP地址为："+myip
    print mes
    for i in range(2):                             #发送1封，上面的列表是几个人，这个就填几  
        if send_mail(mailto_list,"树莓派开机IP",mes):  
            print "发送成功"  
        else:  
            print "发送失败"
