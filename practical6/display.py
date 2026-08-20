def S_display(student):
    print(f"{'Name':<10}{'Roll-No':<10}{'Subject1':<10}{'Subject2':<10}{'Subject3':<10}{'Subject4':<10}{'Subject5':<10}{'Percentage':<12}{'Grade':<9}{'Rank':<10}")
    print("="*97)

    for stu_rec in student:
        
        print(f"{stu_rec[0]:<10}{stu_rec[1]:<10}{stu_rec[2]:<10}{stu_rec[3]:<10}{stu_rec[4]:<10}{stu_rec[5]:<10}{stu_rec[6]:<10}{stu_rec[7]:<12.2f}{stu_rec[8]:<9}{stu_rec[9]:<10}")