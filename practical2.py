list_num = []

num = int(input("Enter Range for numbers : "))

for i in range(num):
    list_num.append(int(input("Enter NUmbers : ")))


print(list_num)

for i in range(max(list_num) - 1):
    if i not in list_num:
        print(i)