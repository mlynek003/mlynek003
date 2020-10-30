lista1=["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]

n=541

if (n<1000):
    z=(n)//100
    x=(n%100)//10
    c=n - z*100 - x*10
    print(lista1[z] + " "+ lista1[x] + " " +lista1[c])