# Write a Python program to count the number of lines in a text file

path = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

f=open(path,'r')

s=f.readlines()

count=len(s)

print(f"The number of lines in the file is : {count}")