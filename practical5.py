

student = []
marks = []
#N = int(input("Enter Number of Student : "))

for i in range(1,3):
    S_name = str(input("Enter Name of Student-"))
    R_number = int(input("Enter Roll Number :- "))
    sub1 = int(input("Enter 1st Subject Marks : "))
    sub2 = int(input("Enter 2nd Subject Marks : "))
    sub3 = int(input("Enter 3rd Subject Marks : "))
    sub4 = int(input("Enter 4th Subject Marks : "))
    sub5 = int(input("Enter 5th Subject Marks : "))


total = sub1+sub2+sub3+sub4+sub5
    
percent = total / 5

if percent >= 90:
    grade = 'A'
elif percent >= 80:
    grade = 'B'
elif percent >= 70:
    grade = 'C'
elif percent >= 60:
    grade = 'D'
elif percent >= 41:
    grade = 'E'
else:
    grade = 'F'

rank = 1

for i in student:
    if student[i] == student[i]:
        rank = rank
    if student[i] == student[i-1]:
        rank = rank 
    else:
        rank = rank + 1




    



student.append([S_name,R_number,sub1,sub2,sub3,sub4,sub5,percent,grade,rank])

print(f"{"Name":<10}{"Roll-No":<10}{"Subject1":<10}{"Subject2":<10}{"Subject3":<10}{"Subject4":<10}{"Subject5":<10}{"Percentage":<12}{"Grade":<10}{"Rank":<10}")
print("="*100)
for stu_rec in student:
    print(f"{stu_rec[0]:<10}{stu_rec[1]:<10}{stu_rec[2]:<10}{stu_rec[3]:<10}{stu_rec[4]:<10}{stu_rec[5]:<10}{stu_rec[6]:<10}{stu_rec[7]:<10}{stu_rec[8]:<10}{stu_rec[9]:<10}")
    
