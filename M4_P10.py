#Write a Python program to count the frequency of words in a file.
path = "C:\\Users\\OM\\OneDrive\\Desktop\\html css assignment\\css\\PYTHON-FUNDAMENTALS OF PYTHON\\class work\\file management\\test1.txt"

f={}
file=open(path,'r')
for i in file:
    words=i.split()
    for j in words:
        word=j.strip('.,!?()[]{}"\'').lower()
        if word in f:
            f[word]+=1
        else:
            f[word]=1        

print(f)
for i,j in f.items():
    print(f"{i}:{j}")