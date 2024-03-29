#Write a Python program to read first n lines of a file
e = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

N = int(input("Enter N value : "))

with open(e, 'r') as file:
    data= file.readlines()

print(f"The following are the first {N} lines of a text file :")

for i in (data[:N]):
    print(i, end ='')