name = "Klay"
age = 30
gpa = 1.38
is_student = True

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(gpa)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

gpa = int(gpa)
age = float(age)

print(f"{gpa} is now an integer: {type(gpa)}")
print(f"{age} is now a float: {type(age)}")