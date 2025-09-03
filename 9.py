dict={'alice':60,'bob':70,'carol':80,'john':90}
n=input("Enter student name=")
j=dict.values()
for i in dict.keys():
    if n==i:
        print(f"{n}'s Marks: {dict[i]}")
        break
    else:
        print("Student not found")
        break