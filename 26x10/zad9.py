lista1=[1,2,4,5,6]
lista2=[0,9,8,7]
d=0
for i in lista1:
    for x in lista2:
        if i==x:
            print("YES")
            d=1
if d==0:
    print("NO")