# QUESTION 1

pass_count = 0
fail_count = 0

print("Passed Students:")

with open("E:\\Training\\new_file.txt","r") as file3:
    lines = file3.readlines()
    for line in lines:
        name, marks = line.strip().split(",")
        marks = int(marks)
        if marks >= 45:
            pass_count += 1
            print(name)
        
print("Failed Students:")

for line in lines:
    name, marks = line.strip().split(",")
    marks = int(marks)
    if marks < 45:
        fail_count += 1
        print(name)

print("\nTotal Passed Students:", pass_count)
print("Total Failed Students:", fail_count)

print("------------------------------------------------")

# QUESTION 2

salary_count = 0

print("Salary greater than 50000")

with open("E:\\Training\\salary.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        name, salary = line.strip().split(",")
        salary = int(salary)
        if salary > 50000:
            salary_count += 1
            print(name)

print(salary_count)

print("------------------------------------------------")

# QUESTION 3

present_count = 0
absent_count = 0

print("Absent Students:")

with open("E:\\Training\\attend.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        name, attendance = line.strip().split(",")
        attendance = attendance.strip()
        if attendance == 'Absent':
            absent_count += 1
            print(name)
        else:
            present_count += 1

print("\nTotal Present Students:", present_count)
print("Total Absent Students:", absent_count)