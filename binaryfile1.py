#Binary Files

list1=[12,34,200,255]

file=r'C:/Users/LENOVO/Desktop/Bacancy/binary_file.txt'
buffer=bytes(list1)
print(buffer)

with open(file,"bw") as f:
    f.write(buffer)

with open(file,"br") as f:
    buffer=f.read()
    print(buffer)
    print("Length of buffer is %d" %len(buffer))

    for i in buffer:
        print(int(i))