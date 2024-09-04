# Jackson Hauley - Setting, Resetting, and Resetting

staff = 32
students = 100
guests = 2
table = 12

staff = staff - 3
students = students - 1

total = students * guests + staff + students
total = total - 15 + 1

tables_used = total/table

round(tables_used)

print("There are",tables_used,"tables needed")
