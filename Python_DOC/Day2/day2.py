#code 1. variable declaration 

num = 100
#this will create a variable num
print(num)
#here f is used as formatted string
print(f"num = {num}") #the syntax is imp with indentation also 
print(f"num = {num}, data type = {type(num)}") #the syntax is imp with indentation also 

#Understanding the Literals 
#Float Numeric Literal 
num = 15.50
print(f"num = {num}") #the syntax is imp with indentation also 
print(f"num = {num}, data type = {type(num)}") #the syntax is imp with indentation also 

#string Literals 
name = "Navneet"
print(f"name = {name}, data type = {type(name)}") #the syntax is imp with indentation also 

#If we want to store the String like a paragraph or multiline string then u have to give triple double qoutes
#name = """___
# ----------
# ----------"""

#   boolean Datatype 
is_active = True
print(f"name = {is_active}, data type = {type(is_active)}") #the syntax is imp with indentation also 

# string is a immutable datatype evry single time it will create a new memory allocation .and if the value of two diff variables with two diff name is same then there is no need to allocat a new memory block

#Starting with type hinting
num:int = 10

#Changing this datatype
#datatype is inferred based in the value (string is not an integer )

num:int = "Navneet"
print(f"num = {num}, data type = {type(num)}") #the syntax is imp with indentation also 

#type Conversion 

#Everythihng to interger
salary = 15.50
salary_int = int(salary)
print(f"salary = {salary_int}, data type = {type(salary_int)}") #the syntax is imp with indentation also 


#starting with user Inputs
number1=input("Enter first number: ")

num2=(input("Enter the number 2"))
print(num2+number1)



number1=int(input("Enter first number: "))
num2=105

num2=int(input("Enter the number 2"))
print(num2+number1)

#Operators

#ADDition

    #for Integers it performes addition  
num1 = 100
num2 = 200
add=num1+num2 
print (add)
   
    #for strings it do string concatination
num = "hello "
num1 = "world"
num2 = num + num1
print(num2)
#Substraction Symbol
    #normally on intergers
    #negative minus can not be prformed on strings

#Multiplcation 
    #normally on Intergers 
    #repetition on Strings


#Starting with functions 
    #empty function:- function has only one statement as pass


def Empty_function():
    pass

#parametre less function 
#function without any arguent 5


def function1():
    print("Inside function 1")
    number1=int(input("Enter first number: "))
    num2=105

    num2=int(input("Enter the number 2"))
    print(num2+number1)

function1()

def function2(name, address, age, salary):
    print("Inside Function")
    print(name)
    print(address)
    print(age)
    print(salary)

function2("Navneet", "Delhi", 22, 5)