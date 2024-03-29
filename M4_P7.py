# Write a Python program to read a file line by line store it into a variable.

l = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

try:
    with open(l, 'r') as file:
        variable = file.read()
except Exception as e:
    print("An error occurred: ",e)

print(variable)