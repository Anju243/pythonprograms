n=int(input("enter the limit:"))
li=[]
c=0
for x in range(n):
    x=input("enter a name:")
    li.append(x)
    for i in li:
     for j in li:
        if 'a'in j.lower():
            c=c+1
            print("the occurrence of 'a' is:",c)