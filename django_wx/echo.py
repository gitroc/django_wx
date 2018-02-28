import re
from django_wx.tf1 import tf11, tf12
from django_wx.tf2 import tf21, tf22, tf23


def echo(message):
    try:
        msg = message.content.strip().lower().encode('utf-8')
        if re.compile("tf11".encode('utf-8')).match(msg):
            tf11()
            return '机器学习 tf11...'
        elif re.compile("tf12".encode('utf-8')).match(msg):
            tf12()
            return '机器学习 tf12...'
        elif re.compile("tf21".encode('utf-8')).match(msg):
            tf21()
            return '机器学习 tf21...'
        elif re.compile("tf22".encode('utf-8')).match(msg):
            tf22()
            return '机器学习 tf22...'
        elif re.compile("tf23".encode('utf-8')).match(msg):
            tf23()
            return '机器学习 tf23...'
        else:
            return '对不起我的能力有限，请输入明确的问题'
    except Exception as e:
        print(e)
