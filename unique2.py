n=input("enter a string")
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)