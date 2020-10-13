#!/usr/bin/python
import os
import re
import urllib
import random
import time

cwdpath = os.getcwd()
def walkFile(dir_name):
 global cwdpath
 for root, dirs, files in os.walk(dir_name):
 
        for f1 in files:
                #print(os.path.join(root, f1))
                print(f1)
                f = open(os.path.join(root, f1),"r")
                #line = f.readline()
                i = 0
                while 1:
						line = f.readline()
						if not line:
							break
						i = i + 1
						ln = line[:-1]
						pat = re.compile(r'<img class="uploaded-img".+?"(.+?)".+?>')
						images_list = pat.findall(ln)
						if len(images_list) > 0:
							each = images_list[0]
							dir = cwdpath+ '/'+'imgbak'+'/'+f1+'/'+time.strftime("%Y%m%d", time.localtime())+'/';
							filename = dir + str(i)+'_'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.png'
							if not os.path.exists(dir):
								os.makedirs(dir)
							urllib.urlretrieve(each,filename,None)
				
                f.close()
		

def main():
	global cwdpath
	path = cwdpath+'/articlebak/'
	#path = os.path.join(path, '')
	#path = path.replace('/','\\')
	path = path.replace('\\','/')	
        walkFile(path)
		
if __name__ == '__main__':
        main()
		
#Email: 1039495585@qq.com