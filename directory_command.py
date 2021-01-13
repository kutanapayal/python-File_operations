import os

#get current directory
print(os.getcwd())

#change directory
print(os.chdir('c:\\Users\\LENOVO\\Desktop\\Bacancy\\files\\file'))
print(os.getcwd())

#list all directory and files
print(os.listdir())

#create directory
os.mkdir('test')
print(os.getcwd())

#Rename Directory and Files
os.rename('test','new_one1')

os.listdir()

#Remove Directory
os.rmdir('new_one')

#Remove file
#os.remove('filename.txt')


