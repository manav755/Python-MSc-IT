N = str(int(input("Enter N integers :- ")))

list=[]

for i in N:
    count = N.count(i)

    if count > 1 and i not in list:
        list.append(i)
    else:
        continue

print(list)