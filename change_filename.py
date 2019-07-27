#该文件是一个小脚本用于将文件夹内的图片按顺序重命名为01,02,03，...，23...这种类型
#c:\\python\\school为存放图标的目标文件夹

import os,sys
os.getcwd()
#going to the target folder
os.chdir("c:\\python\\school") 
filenames=os.listdir(os.getcwd())
list(filenames)
for num in range(len(filenames)):
	if filenames[num]!='changeall.py':
		if num<10:
			os.rename(filenames[num],'0'+str(num)+'.JPG')
		else:
			os.rename(filenames[num],str(num)+'.JPG')
input()
