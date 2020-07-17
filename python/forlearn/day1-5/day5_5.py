import getpass
usrname = input('请输入用户名: ')
usrpass = getpass.getpass('请输入密码: ')
if usrname == 'jaywhen' and usrpass == 'qndxx':
    print('welcome!')
else:
    print('login failed')
