def S_display(student):

    print(f"{'Name':<10}{'Roll-No':<10}{'Sub1':<8}{'Sub2':<8}{'Sub3':<8}{'Sub4':<8}{'Sub5':<8}{'Total':<8}{'Percentage':<12}{'Grade':<8}{'Rank':<6}")
    print("=" * 100)

    for stu_rec in student:

        print(f"{stu_rec[0]:<10}"
              f"{stu_rec[1]:<10}"
              f"{stu_rec[2]:<8}"
              f"{stu_rec[3]:<8}"
              f"{stu_rec[4]:<8}"
              f"{stu_rec[5]:<8}"
              f"{stu_rec[6]:<8}"
              f"{stu_rec[7]:<8}"
              f"{stu_rec[8]:<12.2f}"
              f"{stu_rec[9]:<8}"
              f"{stu_rec[10]:<6}")