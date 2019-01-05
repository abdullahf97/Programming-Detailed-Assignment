print('Practice Problem 3.25')
stu_list = []
for x in range(3):
    a = input("Student Name " +str(x+1)+":")
    stu_list.append(a)
for x in range(3):
    if stu_list[x][:1] in ('A','B','C','D','E','F','G','H','I','J','K','L','M'):
        print(stu_list[x])
