# -*- coding: utf-8 -*-
from chaofeng import Server,Frame, EndInterrupt,Timeout
from chaofeng.g import marks,mark,static
from chaofeng.ui import TextInput,Password
from chaofeng.ascii import *
import config

'''
欢迎页面。并实现了验证登陆。
登陆成功后，用户名记录在session['username']中，
而密码在session['password']中。

可能跳转到register页面（用于注册新用户）和main页面（主菜单）。
'''

def check_username(str):
    return True

def check_user(username,password):
    return True

def login_as_guest(frame):
    pass

def login(frame,username,password):
    pass

@mark('welcome')
class Welcome(Frame):

    background = static['welcome']
    hint_u   = u'\r\n[0;1;33m请输入帐号[0m:[m '.encode('gbk')
    hint_p   = u'\r\n[0;1m请输入密码:[m '.encode('gbk')
    hint_u_e = u'\r\n[0;1;31m经查证，无此 ID (User ID Error)...[m '.encode('gbk')
    hint_p_e = u'\r\n[0;1;31m密码输入错误 (Password Error)...[m '.encode('gbk')
    
    def initialize(self):

        self.write(self.background.\
                       safe_substitute(ip=self.session['ip'],
                                       port=self.session['port'],
                                       online=len(self.server.sessions),
                                       max_behind=2000,
                                       max_record=2000,
                                       have_register=2000))
        
        hint_u = self.hint_u
        hint_p = self.hint_p
        hint_u_e = self.hint_u_e
        hint_p_e = self.hint_p_e
        
        input_u = TextInput(self)
        input_p = Password(self)

        with Timeout(120,EndInterrupt):
            while True :
                self.write(hint_u)
                username = input_u.read()
                if username == 'new' :
                    self.goto(marks['register'])
                elif username == 'guest' :
                    login_as_guest(self)
                    self.goto(marks['main'])
                elif not check_username(username) :
                    self.write(hint_u_e)
                    continue
                self.write(hint_p)    
                password = input_p.read()
                if check_user(username,password) :
                    login(self,username,password)
                    self.goto(marks['main'])
                self.write(hint_p_e)

@mark('main')
class Main(Frame):

    def initialize(self):
        self.write("\r\nThis part hasn't be finish.")
        self.write('\r\nCtrl+c to exit.')

    def get(self,data):
        if data == k_c_c :
            self.close()

    def clear(self):
        self.write('\r\nThanks for you login.\r\n')
        
if __name__ == '__main__' :
    s = Server(Welcome)
    s.run()
