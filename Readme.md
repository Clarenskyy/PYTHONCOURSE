# Python

## Chapter 1

### print()
- prints a message in the console, it can be a string, a variable or an expression

```py
print("etits")
```

### comments
- to comment in python we use `#`

## Chapter 2 - Variables
### Variable
- container for a value (string, integer, float, boolean)

```py

first_name = "Clarence"

print(first_name)

```

to be able to print variables inside double quotes we use `f-string`

```py

print(f"Hello, my name is {first_name}")

```

### if-else
- to check a condition and execute a block of code if it is true

```py

if condition:
    code to execute if condition is true
else:
    code to execute if condition is false


if is_male:
    print ('nice dog')
else:
    print ('nice cat')
```

## Chapter 3 - typecasting
### Typecasting
- process of converting a variable from onde data type to another

### `type()`
- used to determine the type of data a variable is

```py
name = "Klay"
age = 30
gpa = 1.38
is_student = True

print(type(name)) # <class 'str'>
```

### `int()`, `float()`, `str()`, `bool()`
- used to convert a variable to a specific data type

```py
gpa = int(gpa)
age = float(age)

print(f"{gpa} is now an integer: {type(gpa)}")
print(f"{age} is now a float: {type(age)}")
```

- `bool()` works in a way that when something is empty it returns false
 
## Chapter 4 - user input
### `input()`
- a function that prompts the user to enter data which are returned as a string

```py
bigness = input("how big?: ")
age = int(input("how old?: "))

age = age + 1

print(f"bigness is {bigness} and age is {age}. added object age by 1: {age}")
```