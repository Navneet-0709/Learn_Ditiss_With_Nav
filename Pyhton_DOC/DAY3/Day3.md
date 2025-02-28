# day3 ()
- Started with the revision of topics we had done on {Day2}
- had a talk about how num as a variable is stored in symbol table and its memory location 
- Symbols are nothing but identifiers and identifiers are nothing but the names we give to variables , functions ,  lists , etc
- a declartion of a function for python there is a seperate memory location which keeps the refrence stored in it is of body of that function 
- when we call the function it goes to symbol table finds the entry of that function type variable see the type then value and since the value is refrence to another memory location .
- why python take function as variables 
# Remember that python is considerd to be a functinal programming language. 
- in Functional programming 
                        - FUNC IS A FIRST CLASS CITIZEN FOR PYTHON 
                        - functions are treated as variable of func type resting with the value of the refrence of its own body 
                        - function can also be passdd as a argument in another function 
                        - a function can be returned from another function as return value 
                        - I java also func is taken as variable of function type

A func body works as a string for python and is stored in contigous memory blocks 

- talks about bytecode PVM pymain and then stack of pvm
- stack frame also known as function activaition record

- If we create a new variable and assing it with already defined function then it will give refrence to the function body 

# What is the nature of variable in python? Let’s consider an example:

* If created a variable `num = 200`, then assigned `num` to new variable `my_num`, `my_num` points to the same object as that of `num` but if changed or modified the value of `my_num` then a new copy of the object `my_num` is created.  

* Functions behave in the same way, where if you created a function, say `function1()`, and assigned it to another function `my_function1`, `my_function1` is not a new one but pointing to the same function `function1`. This is called Function alias, using it as another name for the reference function.

```
def function1():
    """this is a sample function"""
    print("inside function1")

# created another function using the existing one
my_function1 = function1
my_function1()
```
This proves that functions assignment happens the same as that of variables, unless you change or modify them. 

* When you create a variable, say `num = 200`, it get stored in the memory,  say gets a memory location `0x10000` and gets the name as `num`. And when you define a function, `function1()`, it allocated the memory for the function too, exactly the way the variable got stored into the memory. But remember that when you declare a function, two memory locations are created, one for the function defination, another for reference to the function code block. The block that contains the function defination contains the reference memory to the body of the function, meaning code block. 

You can also print the function value of the function as you do with the variables, you can do this, `print(function1 = {function1}’)` giving you the result as `function <function function at 0x104dbfec0>`.  But this doesn’t mean that you can access the memory address of the function, the return statement only explains the fact that this item or object is stored in the memory, meaning the content of the memory.

* The memory in python in accessed through Operating system, but PVM is the only medium to access the memory, which python communicates with the PVM and get the desired address. Though the address is communicated with the OS, it doesn’t mean the memory can be communicated through python. Python doesn’t allow the access of memory.

What happens when you do a function assignment? The behaviour of function changes when you do a function assignment.

* On function assignment, the function will point to same function, meaning if created a function `function1()` and made another assignment, like `my_function1() = function1`, here you’ve simply referenced `my_function1` to `function1`. 
* This also mean that when you make a changes to `my_function1` the change wiil be reflected in the `function1` because both functions are pointing to only one memory location that has a hold of the code block.

# non-returning functions do not return anything explicitly
# this type of function return NONE implicitly 
# NOTE :- Python does not have any entry point function but PVM have a entry point function named Pymain


#Scopes in Programming 
1. Global Scope                                               2. Loacal Scope 
- Declaretion outsideof any function                            - declared inside the fucntion 
- accessible everywhere in the same program                     - accessible only inside the function within created
    - inside functions 
    - outside functions

In c the value of global variable once changed in any function will not retain its own value but in python the value of global value always retained 
and to change the value or to modify the value of global variabl ewe use a special keyword named global 
Once the refrence og the global variable is changed using the global keyword the value for the global ariable will be changed for all the programm
 Functions do have certain properties:
    * Inner function can access all the parameter and members of the outer function, the one defined inside the outer function.
    * Any member or variable defined in inner function, the outer function can’t access it, therefore, if you tried changing any variable defined in the outer function, you can’t change the variable (defined in outer function) in the inner function, this also means that outer function can’t access the members and variables of the inner function.
    * In order to change the variable defined in outer function, use `nonlocal` keyword, but in order to change the variable defined in the global scope, you need to use the keyword `global` , using `global` variable will help you access the global variable defined in the global scope. But in order to use the variable defind within the scope of outer function, you will only use `nonlocal` keyword.
    * All the function defined in the local scope, the function create a different function within the local scope of the outer function.

# LAmda Function  
    - anounymous named ( with no name ) function  (A function that has a name)
    - does not have any time 
    - must be declared with lambda keyword 
    - rules 
        -lambda must conitain only one statement in the body 
        - the body statement must return a value 
        - lambda must accept atleast one parametre (it is a convention not compulsion) 
    - here return variable used is not a function name rather it is a refrence to the lamda function's body memory 
    - every lambda can be coverted into normal functions but not vice-a-versa
    - Benefits
        - Are more readable than a normal named function
        - simpler than named function
        - bit faster than the named function

# convert m to cm 
    # - Code (Normal Function )
        def to_cm(Dis_in_cm):
            return Dis_in_cm * 100

    # in_cm = lambda d : d*100  (That's it )
    
# Collections :- List, Tuple, Dictionary, Sets
    -Group of similar or dis-similar Values
    -types
        - List []
        - tuple ()
        - set {}
        - Dictionary { : }

#   -List
        - collection of similar or dissimilar values 
        - represented by using square bracets, [ ]
        - likst is quite slow 
        - is must to know coz it will be used in numpy array
        - list having no values are empty list 
        - length function is used to get the size of list "Len(list)"
        - List is a mutaable type of datatype the length of the collection can vary
        - Allows to have duplicate value  
        - count() methods is used to get the number of duplicate values in a list
        - Index() function is used to find the index value of an element form start_Position 
        - reverse() is user to reverse the collection
        - Copy() used to create a seperate copy of the list 
        - Sort is used to sort the list in acceding or deccending order (for deccending we have to use reverse keyword)

        - len() 
            - get the length of the list, using `len(numbers)`, will return a lenght of number.
        
        - append operation 
            - """ def function():
                    numbers = []
                    print(f"numbers = {numbers}")

                    numbers.append(60)
                    print(f"numbers = {numbers}")

                  function()"""
            
            - append can append only one number at a time in the list

        - insert operation =  inserting in between
            - used to insert a value in between     
            """ number[10,20,30,40]
                #insert 15 between  10-20
                number.insert(1,15)"""

        - extend operation - adding number of valueps at the end of the list 
                    - """ def function():
                    numbers = []
                    print(f"numbers = {numbers}")

                    numbers.extend(60,70,80)
                    print(f"numbers = {numbers}")

                  function()"""
        
        - count() will return a number of times the item occured in the sequence.
                >>> l2
                [9, 12, 12.0, (1, 2, 3), (1, 2, 3), 2, 3, 'string', 'String']
                >>> l2.count((1,2,3))
                2

        - clear() 
            - will remove all the values or items from the list.
        
        - sort() 
            - will the sort the sequence in the ascending order and can pass the `reverse` argument as `True` to
              reverse the order of sort, meaning it will start the sorting in reverse, that means it will start sorting from last index.


        - POP Operation - to remove from the last
            - Exactly opposite from the append'
               """ number[10,20,30,40]
                number.pop()"""

        - to remove something from inbetween 
            - either by knowing the index
                - numbers.pop(3)

            - directly without knowing the index position 
                numbers.remopve(30)

                - in case of duplicate values there are coule of methis that help us to delte the duplicate values



# imp 
What will u get after calling a non returning function 
why python is called as general purpose programming language 
what are the data types supported in python 
what is the retun value of a non-returning function 
what is global keyword why is it used in python 
what is a lanbda function and tell us the diff between names and lambda function
what arethe rules of writing a lambda function
what are the use cases of lambda
what is a fucntion refrence ?
how the function gets executed in python ?