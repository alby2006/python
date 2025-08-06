list=[]
n=int(input("enter number of elements"))
for i in range(n):
    value=int(input("enter element"))
    list.append(value)
    unique=[]
    for item in list:
        if item not in unique:
         unique.append(item)
print("unique element:",unique)