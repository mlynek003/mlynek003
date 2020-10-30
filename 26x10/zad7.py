lista1=[1,2,3,7,0,6]
d=(lista1[0])
index = 0
counter = 0
c=(lista1[0])
for i in lista1:
    if (i > d):
        d = i
        index = counter
    counter += 1
lista1[index]=0
index =0
counter =0
for i in lista1:
    if (i > c):
        c = i
        index = counter
    counter += 1
print(c)
print(index)