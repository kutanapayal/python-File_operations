#f = open("test.txt")      # equivalent to 'r' or 'rt'
#f = open("test.txt",'w')  # write in text mode
#f = open("img.bmp",'r+b') # read and write in binary mode

#f = open("test.txt", mode='r', encoding='utf-8')


'''try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
'''

'''
with open("test.txt",mode='r+',encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

    print(f.read(4))    # read the next 4 data
    print("get current file location:",f.tell())    # get the current file position)
    f.seek(0)  # bring file cursor to initial position
    print(f.read())  # read in the rest till end of file
'''

f=open("test.txt",mode='r+',encoding='utf-8')
for line in f:
    print(line, end = '')

print(f.readline()) #reads a file till the newline


#print(f)