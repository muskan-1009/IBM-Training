# Question 1

name = input("Enter the name: ")
s = int(input("Enter the salary: "))

def hra(s):
    return s*0.2

def da(s):
    return s*0.1

def net_slary(s):
    return s + hra(s) + da(s)

print(net_slary(s))

print("-----------------------------------")

# Question 2

l1 = []
for i in range(5):
    marks = int(input("Enter the marks: "))
    l1.append(marks)
print(l1)

def calculate_total(marks):
    return sum(marks)

a = calculate_total(l1)
print(a)

def calculate_percentage(marks):
    return (a/500)*100

b = calculate_percentage(l1)
print(b)

def assign_grade(marks):
    if b>= 90:
        return "A"
    elif 75<b<90:
        return "B"
    elif 60<b<75:
        return "C"
    elif 45<b<60:
        return "D"
    else:
        return "F"
    
c = assign_grade(l1)
print(c)

print("-----------------------------------")

# Question 3

student = {}
grade = ("A", "B", "C", "D", "F")


for i in range(5):
    roll = int(input("Enter the roll no: "))
    name = input("Enter the name: ")
    marks = []
    for j in range(5):
        mark = int(input("Enter the marks: "))
        marks.append(mark)

    student[roll] = {'roll_no': roll, 'names': name, 'mark': marks} 

print(student)

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return (total/500)*100

def assign_grade(percentage):
    if percentage>= 90:
        return grade[0]
    elif 75<=percentage<91:
        return grade[1]
    elif 60<=percentage<76:
        return grade[2]
    elif 45<=percentage<61:
        return grade[3]
    else:
        return grade[4]
    

for roll in student:
    marks = student[roll]["mark"]
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade_obtained = assign_grade(percentage)

    print("\nRoll No:", student[roll]["roll_no"])
    print("Name:", student[roll]["names"])
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade_obtained)

def display_student(details):
    print("\nRoll No:", details["roll_no"])
    print("Name:", details["names"])
    print("Marks:", details["mark"])

for roll in student:
    display_student(student[roll])

highest_percentage = 0
topper_name = ""

for roll in student:
    total = calculate_total(student[roll]["mark"])
    percentage = calculate_percentage(total)

    if percentage > highest_percentage:
        highest_percentage = percentage
        topper_name = student[roll]["names"]

print("\nTopper:", topper_name)
print("Percentage:", highest_percentage)