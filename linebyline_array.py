# Python program to read a file line by line store it into an array.
fin = open("python1.txt","r")
array = []
data = fin.read()
l = data.split()
for line in l:
    array.append(line)
print(array)