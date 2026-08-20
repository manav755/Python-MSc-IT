def S_data():
    student = []

    N = int(input("Enter Number of Student You Want : "))

    for i in range(N):
        S_name = str(input("\nEnter Name of Student-"))
        R_number = int(input("Enter Roll Number :- "))
        
        marks = []

        print("\nEnter subject marks ")
        for j in range(5):
            
            mark=int(input("Enter marks of Subject "+str(j+1)+" : "))
            marks.append(mark)
 
        total = sum(marks)
        
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

        student.append([S_name,R_number]+ marks +[total,percent,grade,rank])

    return student
