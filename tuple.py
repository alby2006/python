t=int(input("enetr the number of tuple"))
tuple=[]
for i in range(t):
    a=int(input("enter the first element"))
    b=int(input("eneter second element"))
    tuple.append((a,b))
for i in range(t):
        for j in range(t-1):
            if tuple[j][1]>tuple[j+1][1]:
                temp=tuple[j]
                tuple[j]=tuple[j+1]
                tuple[j+1]=temp
print("enter the sorted list",tuple)