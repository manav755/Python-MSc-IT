def S_rank(student):
    student.sort(key=lambda x: x[7], reverse=True)

    rank = 1

    for i in range(len(student)):

        if i > 0 and student[i][7] == student[i-1][7]:
            student[i][10] = student[i-1][10]
        else:
            student[i][10] = rank

        rank = i + 1
    return student