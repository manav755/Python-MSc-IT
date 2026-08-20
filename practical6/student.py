def S_data():
    student = []

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

    return student
