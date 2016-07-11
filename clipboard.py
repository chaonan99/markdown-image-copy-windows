import os
from PIL import ImageGrab
import time
from datetime import datetime
import ConfigParser
from ctypes import *
from qiniu import Auth, put_file
import qiniu.config

# Change this path to temporary store location of copied image
filepath = r'D:/your/path'

im = ImageGrab.grabclipboard()

if not im is None:
	filename = datetime.now().strftime('%Y_%m_%d')\
	+'_'+''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16))) + ".png"
	savepath = filepath + filename
	im.save(savepath,'PNG')

	cf = ConfigParser.ConfigParser()
	cf.read('config.ini')
	access_key = cf.get('qiniu', 'ak') # AK
	secret_key = cf.get('qiniu', 'sk') # SK
	bucket_name = cf.get('qiniu', 'bucket') # qiniu storage space name
	url = cf.get('qiniu', 'url') # url
	q = Auth(access_key, secret_key)
	mime_type = "image/png"
	params = {'x:a': 'a'}
	token = q.upload_token(bucket_name, filename)
	progress_handler = lambda progress, total: progress
	ret, info = put_file(token, filename, savepath, params, mime_type, progress_handler=progress_handler)
	if ret != None and ret['key'] == filename:
		# upload success
		markdown_url = "![%s](%s/%s \"%s\")" % (filename.split('.', 1)[0], url, filename, "Add Description")
		# make it to clipboard
		ahk = cdll.AutoHotkey #load AutoHotkey
		ahk.ahktextdll("") #start script in persistent mode (wait for action)
		while not ahk.ahkReady(): #Wait for AutoHotkey.dll to start
		    time.sleep(0.01)
		ahk.ahkExec(u"clipboard = %s" % markdown_url)
	else:
		print "upload_failed"