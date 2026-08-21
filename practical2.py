#Missing Roll Number

list_num = []

num = int(input("Enter Range of numbers : "))

for i in range(num):
    n = int(input("Enter Number : "))
    if (n <= num):
        list_num.append(n)
    else:
        print("Please enter number under given range!!")


print(list_num)

print("Missing Numbers :-")
for i in range(1, max(list_num) - 1):
    if i not in list_num:
        print(i)