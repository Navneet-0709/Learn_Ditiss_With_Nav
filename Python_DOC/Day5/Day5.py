#day 5
#tuples
def funciton1():
    #list
    numbers_list = [10,20,30,40,50,60]
    print(numbers_list)
    #tuple
    numbers_Tuple = (10,20,30,40,50,60)
    print(numbers_Tuple)
    #tuples can be defined without using parathesis
    numbers_Tuple2 = 10,20,30,40,50,60
    print(numbers_Tuple2)

#funciton1()

def function2():
    #tuple with one value
    number = (20,)
    print(f"numbers = {number}, type = {type(number)} ")

#function2()

def function3():
    #tuple packing
    numbers = 10,20,30 # this is a tuple packing 
    print(f"numbers = {numbers}, type = {type(numbers)} ")
    numbers = 10,20,30 # this is a tuple packing 
    print(f"number[0] = {numbers[0]}")
    print(f"number[1] = {numbers[1]}")

    # we can also do this by storing the value in any variable like
    n1 = numbers[0]
    n2 = numbers[1]
#function3()

def function4():
    # but why to do it on ur own python 
    # python willl do it using tuple unpacking
    numbers = 10,20,30,40,50,60
    n1, n2 = numbers
    print(f"n1= {n1}, n2 = {n2}")
# function4()

def function5():
    n1 , n2 = 10 , 20
    # this above statement is of tuple unpacking used to create variable and assinging values in a sngle statement 
    n1 , n2 = 10 , 20 , 30
    # THIS WILL CREATE  an error since there are too many value to unpack 
    n1 , n2 , n3= 10 , 20 
    # THIS WILL CREATE  an error since there   not enough  value to unpack 

    # but there is an exception 

#function5()

def funtion6():
    #n1 , n2 = 10 ,20 ,30 ,40 ,50 ,60
    #this will surely raise an error
    #but we dont want other values so there is another exception 
    n1 , n2 , *n3 = [10,20,30,40,50,60]
    # this * will be used to collect rest of the values in n3 itself 
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"n3 = {n3}")
#funtion6()

def math_operation(p1,p2):
    addition = p1+p2 
    substraction = p1-p2
    multiplication = p1*p2
    division = p1/p2

    return addition,substraction,multiplication,division
    # here the function is not returning the multiple values instead all values will be packed in a single tuple 
    # this is what we call as tuple packing feature 

def math_operation(p1,p2):
    addition = p1+p2 
    substraction = p1-p2
    multiplication = p1*p2
    division = p1/p2

    return addition,substraction,multiplication,division
    # here the function is not returning the multiple values instead all values will be packed in a single tuple 
    # this is what we call as tuple packing feature 
answer = math_operation(10,1)
print(answer) 

# one more thing we can do here is assinging values using tuple unpacking 
#say a,s,m,d = mathe_operation(p1,p2) 
def function7():
    name1 = input("Enter the first name :-" )
    name2 = input("Enter the second name :-" )
    name3 = input("Enter the third name :-" )

    names = name1,name2,name3
    print(names)
    n1,n2,n3 = name1,name2,name3 
    print(f"n1 = {n1}   ,n2 = {n2}  ,n3 = {n3}")

# function7()

def dummy_function():
    print(f"inside dummy_function")

def function1(param):
    print(f"inside function1")
    print(f"param = {param}, type = {type(param)}")

    param()

# param = 10, type = int
# function1(10)

# param = "test", type = str
# function1("test")

# param = True, type = bool
# function1(True)

# param = num
# num = "test"
# function1(num)

# print(f"dummy_function = {dummy_function}, type = {type(dummy_function)}")

# param = dummy_function
# dummy_function is passed as an argument
# function1(dummy_function)

def another_function():
    print(f"inside another function")

# param = another_function
# function1(another_function)


# ------------------------------------ MAP () --------------------------------------------- 


def function1():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get the square of every number
    for number in numbers:
        print(f"square of {number} = {number ** 2}")

# function1()

def function2():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get square of every number and store them in a collection
    squares = []
    for number in numbers:
        # transformation of number
        squares.append(number ** 2)

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function2()


def function3():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transformation logic
    def make_square(number):
        return number ** 2

    # get square of every number and store them in a collection
    squares = []
    for number in numbers:
        squares.append(make_square(number))
    
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function3()

def function4():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transformation logic
    make_square = lambda n: n ** 2

    # get square of every number and store them in a collection
    squares = []
    for number in numbers:
        squares.append(make_square(number))

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function4()


def function5():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transformation logic
    make_square = lambda n: n ** 2

    # get square of every number and store them in a collection
    squares = list(map(make_square, numbers))

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function5()

def function6():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get cube of a number
    cube = lambda n: n ** 3

    # get cube of every number and store in a list
    cubes = list(map(cube, numbers))
    print(f"numbers = {numbers}")
    print(f"cubes = {cubes}")

# function6()


def function7():
    # list number numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get cube of every number and store in a list
    cubes = list(map(lambda n: n ** 3, numbers))
    print(f"numbers = {numbers}")
    print(f"cubes = {cubes}")

# function7()

# map()
def function8():
    # in celsius
    temperatures = [29, 28, 31, 33, 35, 36, 29, 28]

    # convert all the temperatures into fahrenheit
    temperatures_fahrenheit = []
    for temperature in temperatures:
        temperatures_fahrenheit.append(32 + (temperature * (9 / 5)))
    
    print(f"temperatures = {temperatures}")
    print(f"fahrenheit temperatures = {temperatures_fahrenheit}")

# function8()

def function9():
    # in celsius
    temperatures = (29, 28, 31, 33, 35, 36, 29, 28)

    # lambda to convert temperature from celsius to fahrenheit
    to_fahrenheit = lambda t: 32 + (t * (9/5))
    temperatures_fahrenheit = tuple(map(to_fahrenheit, temperatures))
    print(f"temperatures = {temperatures}")
    print(f"fahrenheit temperatures = {temperatures_fahrenheit}")

# function9()



# ------------------------------------ Filters () --------------------------------------------- 
def function1():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # get all the even numbers from the collection
    for number in numbers:
        if number % 2 == 0:
            print(f"number = {number}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]
    
    # collect all even numbers in a new collection
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    # convert the even numbers collection to tuple
    even_numbers_tuple = tuple(even_numbers)

    print(f"numbers = {numbers}")
    print(f"even numbers list = {even_numbers}")
    print(f"even numbers tuple = {even_numbers_tuple}")

#function2()

def function3():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # lambda to check if the number is even
    is_even = lambda n: n % 2 == 0
    even_numbers = list(filter(is_even, numbers))
    print(f"numbers = {numbers}")
    print(f"even_numbers = {even_numbers}")

#function3()

def function4():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    is_odd = lambda n: n % 2 != 0
    print(f"numbers = {numbers}")
    print(f"odd numbers = {list(filter(is_odd, numbers))}")

#function4()

def function5():
    # marks of students
    marks = [8, 2, 3, 6, 9, 0, 1, 0, 5, 10]
    print(f"marks = {marks}")

    # lambda to check if a student has passed in the exam
    is_passed = lambda m: m >= 5
    passed_students = list(filter(is_passed, marks))
    print(f"passed in the exam: {passed_students}")

    # lambda to check if student has failed in the exam
    is_failed = lambda m: m < 5
    failed_students = list(filter(is_failed, marks))
    print(f"failed in the exam: {failed_students}")

#function5()


# rule
# - always execute the filter function first and then go for map

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get squares of even numbers

    # find the even numbers
    is_even = lambda n: n % 2 == 0
    even_numbers = list(filter(is_even, numbers))

    # get the square of every even number
    square = lambda n: n ** 2
    squares_even_numbers = list(map(square, even_numbers))
    print(f"numbers = {numbers}")
    print(f"square of even numbers = {squares_even_numbers}")
#function1()

def function2():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # cube of odd numbers
    odd_numbers = filter(lambda n: n % 2 != 0, numbers)
    cube_odd_numbers = list(map(lambda n: n ** 3, odd_numbers))
    print(f"numbers = {numbers}")
    print(f"cube of odd numbers = {cube_odd_numbers}")

    # cube of odd numbers
    cube_odd_numbers = list(map(lambda n: n ** 3, filter(lambda n: n % 2 != 0, numbers)))
    print(f"numbers = {numbers}")
    print(f"cube of odd numbers = {cube_odd_numbers}")

function2()

 list comprehension
# - using the list syntax to perform both map and filter operations
# - syntax
#   - [<temp_variable> for <temp_variable> in <collection>]

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get the square of each number
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function1()

def function2():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get the square of each number
    squares = list(map(lambda n: n ** 2, numbers))
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function2()

def function3():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # using list comprehension as a map()

    # get the square of each number
    squares = [number ** 2 for number in numbers]

    # get the cube of each number
    cubes = [number ** 3 for number in numbers]

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")
    print(f"cubes = {cubes}")

# function3()

def function4():
    # in celsius
    temperatures = [29, 28, 31, 33, 35, 36, 29, 28]

    # convert all the temperatures into fahrenheit
    temperatures_fahrenheit = [(32 + temperature * (9/5)) for temperature in temperatures]
    print(f"temperatures = {temperatures}")
    print(f"temperatures in fahrenheit = {temperatures_fahrenheit}")

# function4()



def function1():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # find the even numbers
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function1()


def function2():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # get the even numbers
    even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # get even numbers using list comprehension
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function3() 

def function4():
    # marks of students
    marks = [8, 2, 3, 6, 9, 0, 1, 0, 5, 10]
    print(f"marks = {marks}")

    # get the list of failed students
    failed_students = [m for m in marks if m < 5]
    print(f"failed students = {failed_students}")

    # get the list of passed students
    passed_students = [m for m in marks if m >= 5]
    print(f"passed students = {passed_students}")

function4()


def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # get square of even numbers
    square_even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            square_even_numbers.append(number ** 2)
    print(f"square of even numbers = {square_even_numbers}")


# function1()

def function2():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find the square of even numbers using list comprehension
    square_even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
    print(f"square of even numbers = {square_even_numbers}")

# function2()


def function3():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # lambda to get a square
    square = lambda n: n ** 2

    # lambda to check if a number is even number
    is_even = lambda n: n % 2 == 0

    # find the square of even numbers using list comprehension
    square_even_numbers = [square(number) for number in numbers if is_even(number)]
    print(f"square of even numbers = {square_even_numbers}")

# function3()

def function4():
    ages = [10, 21, 34, 19, 27, 59, 100, 90, 95]

    valid_ages = [age for age in ages if ((age >= 20) and (age <= 60))]
    print(f"ages = {ages}")
    print(f"valid ages = {valid_ages}")

function4()


def function1():
    age = 10
    if age >= 18: 
        print(f"YES")
    else:
        print(f"NO")


# function1()


def function2():
    age = 20

    # this line will return "YES" if condition is true
    # will return "NO" of condition is false
    voting_status = "YES" if age >= 18 else "NO"
    print(f"voting status = {voting_status}")

# function2()

def function3():
    ages = [10, 21, 34, 19, 27, 59, 100, 90, 95]
    statuses = ["YES" if age >= 18 else "NO" for age in ages]

    print(f"ages = {ages}")
    print(f"statuses = {statuses}")

function3() 