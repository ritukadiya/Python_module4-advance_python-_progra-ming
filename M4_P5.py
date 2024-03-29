# Write a Python program to read a file line by line and store it into a list

path = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

l = []

with open(path, 'r') as file:
    for i in file:
        l.append(i.strip())

print(l)