# Day 2 Foundation 

# Identifiers and Keywords 
{
- names that you supply for variable ,functions and classes 
- Shoud be diff in spelling and are case-sensitive
Are of two types 
1. Custom IDentifiers :- Which we use to define and create to assing name or variable etc
2. Keywords 
Keywords are reserved identifiers 
In Python 3.8 there are 35 keywords 
    -Valueable Keyword :- True, False, None
    -operator Keyword  :- and, or, not, in, is
    -control flow Keyword :- if, else, elif
    -iteration Keyword :- for, while, break, continue, else
    -structure Keyword :- def, class, with, as, pass,lambda (is used for anounymous fuctions)
    -returning Keyword :- return , yield
    -import Keyword :- import, from, as
    -Exceptional handling Keyword :-try, except, raise, finally, else, assert 
    -Asynchronous Promming Keyword :- async, await
    -Variable Handling Keyword :-  del, global, nonlocal
4 type of collections :- List , tuple , Dictionary, String
There is no exceptional handling in c thats why the codes in c are weak while that of py are robust... 
Python Provides garbage collection feature so we dont have to delete
}

# Rules and Conventions {
    constants and variables name should have a combi of lowercase uppercase digits or underscore
    If you wannt to creat a variable name having 2 words :- use undeerscore to seperate them :-ex == Navneet_Arora
    Create sensible name which is easier to understand 
    Use capital letters to declare Contant 
    for example :- pi-3.14(variable)  PI-3.14 (Constant)
    avoid using speacial characters (!,@,#,$,%,etc)
    but keep in mind it is convention not compulsion 
    Do not start a variable name with a numerical value (1Navneet :- Wrong (x)) This is MAndatory
    Python is Case Sensitive (navneet, Navneet) are two diff variables or names

```
>>> num                                                      # This is not allowed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined. Did you mean: 'sum'?                                  
>>> PI = 4.56`                                               # is a statment
>>> name = "abc"                                             # in python we execute a single line statement
```

}
# Variables{
    Is a named location used to store dara in the memory which can change its value as in wenver it is needed
    eg:- Value = 20
         name = 'Navneet'   
    Variables are stored in RAM which is a volatile memory
    Lets say num=200
    when u r loading ur os(System program ):- it required memory blocks and aquire a good amount of memory for boot. 
    not num = 200:- what happens is it go and check a random empty memory block and occupy it . 
    ANy random block of memory say 0x25 will be assinged 
    Which creates a table :- A Symbol table keeping the info  every language has its own symbol table that gets generated at compilation time .... 
    Symbol table is nothing but an identifier, as when you try to define a varibale `num` symbol table keeps track of the variables formed.
}
# Constants{

are written in capital letters (It is not compulsory but should be considered to differ them from variables)
eg PI-3.14;
This value v=can be changed but should not keeping in mind that it ia in capital so it is constant


}
# Data Types {
-Is an attribute associated with a piece of data that tells the comp sys how to interpret its value 
-Ensures the data is collected in prefferd format and the value of each property is as expected 

1. Numeric          2. Dictionary          3.Boolean           4.Sequence          5.Set
  - Integer           -key:Value            -true               -List      -Collection of unique values
  -float                                    -false              -Tuple
  -complex                                  -None               -String

Under the category of Numeric data types there are:
    * Integers : 20, -100, 100
    * Float : 15.6
    * Complex : 20 + i5
* Remember, `int` object is totally different from the `float`

Distionary is not a sequence?

}
Note:- In Python all Datatypes are inferred (Automatically Assingned)

# Literals :-{
    is a raw given in a variable or constant
    So How python knows what is data type is the variable? Literals, is a raw variable to tell python what kind of data type a variable is. Through literals python decides what kind of data type a variable is.
    Numeric Literals
        -are immutable 
        -Are of 3 type
            -Int (Value = 100)
            -Float(Salary - 15.5)
            -Cpmlex(x=10+5j)

    String Literal
    Boolean Literal
    
}
# Diff between Static Typing and Dynamic Typing 
         Static typing	                                                    Dynamic typing
Compiler checks the type of variable	            Data type will be assigned at the tim of running app
Compiler assigns data type at compilation	        Data type wil be inferred (Automatically assigned a lanugage)
Dev must provide data type to every var	
C, C++, Java	                                       Python and Javascript are dynamically assigned language

Let’s understand what it means by Static and Dynamic Typing in details:

- Checking type of variable happens when compilation beings, meaning the type of variable is assigned by the compiler, this means that the developer should assign the type of variable, a variable should be fixed, and should be known as well. At the compile time, compiler ckeck the variable and all the shoulds of it, and assignment of data type happens on compilation.
 - On the other hand, In dynamically typed languages, the data type is checked by the interpreter during the run-time of the program, meaning when program is running, the variables are checked by the interpreter to automatically infer the type of the variable. This adds a layer of flexibility to variables that they can carry different types at the different times, becaue python will check which type is to be inferred while it is executing the program.
- But remember, python is both dynamically typed as well as weakly typed language, meaning that you can assign and change the value with different data types in python.
- But there is something called '''type hinting''' feature, thus, giving the hint about the variable what it might be, you are giving the hint of what an object might be.

# Type Hinting {
    - due to dynamic nature of python , iferring or checking the tyoe of an object being used is especially hard
    - this makes it hard for the developers to understand what exactky is going on in code they haven't written.

    What is type hint?
    just a hint or a additional word to help other developers for the data type of any variable 
    But this is just optional 

    #Changing this datatype
    #datatype is inferred based in the value (string is not an integer )

    But remember, type hint is helpful while wrting codes in PyCharm which gives IDEs an intelligent indicator for the developers when trying to change the contents of variables, but this doesn’t change the fact the you can put interger literals in the string type hint.

}

# Type Conversion {
    PRocess of Converting the value of one datatype to another data type
    python has 2 types of conversion :---
    
    1. Implicit Type COnversiom - Python tries to convert the data type from one to another, only wehnn smaller type gets converted to bigger one, meaning if result = 10 + 35.50, float is bigger than integer, therefore, python will convert the data type of result to flaot. This is called Implicit conversion.
    
    2. Explicit Type COnversiom  - Python also supports the explicit type casting as it can be explicitly converted to the type you assign, meaning of result = 10 + 35.50, where if you assign a int before operation, it will convert the result to int, hence, will give result as 45. Though, remember that in Explicit conversion, there might be loss of data becuase you are enforcing the data to a specific type.
}

# Input Methods{
    by default if we input any kind of variable value it is bydefault string
    so we have to convert it into the respective data type.

    number1=input("Enter first number: ")
    num2=(input("Enter the number 2"))
    print(num2+number1)

    tHIS IS by default a string concatnation 

    number1=int(input("Enter first number: "))
    num2=int(input("Enter the number 2"))
    print(num2+number1)
}

# Operators{
    Nothing but the symbols used to perform opreations or actions within the variables like arithemetic and locical computation
    the value that the opreator oprates is called operand..

    Types :-
    - Arithemetic
    - Comparison 
    - Logical
    - Bitwise Operators
    - Special Operators
    - MEmbership Operators 


  
        Code 
# Arithemetic Operators{
    
    Precedence wise:-
    ()
    **
    *
    %
    /
    //
    +
    -
Associativity:- 
    all the ooperators have left to right associativity execot power operator (which is right to left)

#ADDition

    #for Integers it performes addition
    #for strings it do string concatination

#Substraction Symbol
    #normally on intergers
    #negative minus can not be prformed on strings

#Multiplcation 
    #normally on Intergers 
    #repetition on Strings

#Division 
    #division between two numbers will return true division between the two 
    #can not be performed on strings

#floor Division 
    #returns the integer value of the division 

#modulouS
    #returns the remainder of the division of the two number .

#exponential 
    #returns the power raise to number left raise to the power right 
}

#Logical Operations:-

        AND     
        T AND T = T
        T AND F = f
        F AND T = f
        F AND F = F
        
        OR
        T OR F = T
        F OR T = T
        F OR F = T
        T OR T = F
               
        NOT
        NOT T = F 
        NOT F = T


Assingment Operators 

=       x=5     x=5
-=      x-=5    x=x-5
+=      x+=5    x=x+5
*=      x*=5    x=x*5
/=      x/=5    x=x/5
%=      x%=5    x=x%5
//=     x//=5   x=x//5


#Bitwise operators 
 $
 |
 ~
 ^
 <<
 >>
 


#Special Operators 
 is 
 is not

#membership operators 
in 
not in


# ------------:- Functionssssssssssssssss -:-----------

- A reusable block of statement 
- a block must be indented 
- It avoids repetitions and make code reusable 
-  So How the python function is different? Functions are very different from that other languages, let’s first look at different points.
- In python there are two kinds of errors, Compiled Time Error, as well as Run Time Error. In python, indentation creates a block of code that allows python to differtiate within different lines of code.

Syntax:- def function_name(parametres):
"""docstring"""
statement(S)

It contains two things :- Declaration{Function names and argumens } and Definition{Function Body}
In python u have to declare and define the fucntion at the same time 

there are 2 ways to assing parametres in functions 
1. Indexting wise
2. named PArametres

# Docstring:- 
The first string after fucntion header is called the docstring and is short for documentation string 
it is breifly used to explain what a fucntion does 
although optional, documentation is a good programming practice 
we generally 

# types of functions 

1. built in fucntions 
    that are predefined and readily come with python are called buit in function 
    if we use functions written by others in the library, it can be termed as library functions 
    ef str(),int(),
2. user defined functions 
    
    functions that we defile oursleves to do certain specific tasks are reffered as user - defined fucntions 
    
    user defined func help tp decompase large program into smal segments which make program easy to understand maintain and debug 
    
    if repeated code occurs in a program. function can be used to execute those codes and can be called for execution whenever needed


# Topics Covered Today :- 
Identifiers and Keywords
Variable 
Constant
Rules and Conventions
Data Types 
Literals 
Diff between Static Typing and Dynamic Typing 
type hinting 
Type of Conversoions 
Symbols
Functions 
Docstring
Type Functions


# IMP
Interview Ques :- Asynchronous PRogramming (Asyn await for parrallel programming)
Type hinting giving hint to someone about the type of ur variable 




# Codes Day 2 -------

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