Password = input("Enter the password : ")

Up_case = False
Low_case = False
Digit = False
Special_char = False
Consecutive = []

for char in Password:
    if char >= 'A' and char <= 'Z':
        Up_case = True
    elif char >= 'a' and char <= 'z':
        Low_case = True
    elif char >= '0' and char <= '9':
        Digit = True
    else:
        Special_char = True


for i in Password:
    Pass = Password.count(i)
    char_rep = Password.index(i)
    if Pass > 1 and (Password[char_rep] == Password[char_rep + 1]):
        if i not in Consecutive:
            Consecutive.append(i)

if not Up_case:
    print("Password not contains Uppercase letters!.")
if not Low_case:
    print("Password not contains Lowercase letters!.")
if not Digit:
    print("Password not contains Digits!.")
if not Special_char:
    print("Password not contains Special Character!.")
if Consecutive:
    print("Password Contains Repeted Characters!.",Consecutive)
else:
    print("Password is Correct.")

