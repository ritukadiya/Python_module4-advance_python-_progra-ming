# Write a Python program to write a list to a file.

path = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

l=[10,20,30,50,1,2,3,50,70]

file=open(path,'w')
for i in l:
    file.write(str(i)+'\n')
file.close()

with open(path,'r') as file:
    read=file.read()
print(read)