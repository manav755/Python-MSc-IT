

student = []
marks = []
N = int(input("Enter Number of Student You Want : "))
i = 0
for i in range(N):
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

    rank = 0

    student.append([S_name,R_number,sub1,sub2,sub3,sub4,sub5,percent,grade,rank])

student.sort(key=lambda x: x[7], reverse=True)

rank = 1

for i in range(len(student)):
    if i > 0 and student[i][7] == student[i-1][7]:
        student[i][9] = student[i-1][9]
    else:
        student[i][9] = rank
        rank += 1
        


print(f"{'Name':<10}{'Roll-No':<10}{'Subject1':<10}{'Subject2':<10}{'Subject3':<10}{'Subject4':<10}{'Subject5':<10}{'Percentage':<12}{'Grade':<9}{'Rank':<10}")
print("="*97)
for stu_rec in student:
    print(f"{stu_rec[0]:<10}{stu_rec[1]:<10}{stu_rec[2]:<10}{stu_rec[3]:<10}{stu_rec[4]:<10}{stu_rec[5]:<10}{stu_rec[6]:<10}{stu_rec[7]:<12}{stu_rec[8]:<9}{stu_rec[9]:<10}")
    
