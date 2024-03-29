#Write a python program to find the longest words.

path = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

f = open(path,'r')
s = f.read()

lst = s.split()

print(s)
print("\nLongest Word in a File is :",max(lst,key=len))