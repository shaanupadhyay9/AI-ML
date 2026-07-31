 # First Python Program
print("Hello World")

# Variables
name = "Shaan"
age = 21
height = 5.9
print("Name:", name)
print("Age:", age)
print("Height:", height)

#Data Types
x = 10
price = 99.99
name = "Python"
is_pass = True

a = 10
print(type(a))

#Taking input form user
name = input("Enter name: ")
print(name)
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
print(age, salary)

#Type conversions
a = "25"

print(int(a))
print(float(a))

#Arithmetic Operations
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b) 

#Conditional Statements
age = 20

if age >=18:
    print("Eligible")
else:
    print("Not Eligible")

age = 15

if age>=18:
    print("Adult")
else:
    print("Minor")
    
marks = 85

if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")
    
    
# loops
for i in range(5):
    print(i)
    
i=1

while i<=5:
    print(i)
    i+=1
    
for i in range(10):
    if i==5:
        break
    print(i)
    
for i in range(6):
    if i==3:
        continue
    print(i)
    
#Strings
name="Python"
print(name[0])
len(name)
name.upper()
name.lower()
name.replace("P","J")
print(name[1:4])

#Lists
numbers=[10,20,30]
numbers[0]
numbers.append(40)
numbers.insert(1,15)

numbers.remove(20)
numbers.pop()
len(numbers)
for x in numbers:
    print(x)
    
#Tupless
t=(1,2,3)

#Sets
s={1,2,3,3,4}

#Dictionaries
student={
"name":"Shaan",
"marks":90
}

student["name"]
student["age"]=20
student["marks"]=95

for key,value in student.items():
    print(key,value)
    
#Functions
def greet():
    print("Hello")
    
    
greet()

def add(a,b):
    print(a+b)
    
add(10,20)

def add(a,b=10):
    print(a+b)
    
add(10)

greet()
# Lambda functions
square=lambda x:x*x

print(square(5))


