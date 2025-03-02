#list
def function():
    #list of numbers 
    numbers = [10,20,30,40,50]
    print(f"numbers = {numbers}")

# function()    
def function1():   
    
    numbers = [10,20,30,40,50]
    #value is a temp var to hold value at each iteration
    for value in numbers:  #iteration will happen according to the number of elements in the list 
        print(f"value = {value}")

# function1()

def function2():  #square of all numbers 
    
    numbers = [10,20,30,40,50]
    #value is a temp var to hold value at each iteration
    for value in numbers:  #iteration will happen according to the number of elements in the list 
        print(f"value = {value ** 2}")

# function2()

#here we just wanted the values of numbers presented at the position 
#instead of running the iteration on the numbers collection we are using a diff collection 
def function3():
    numbers = [10,20,30,40,50]
    position = [1,2,3] 
    for x in position:
        print(f"value at {x} = {numbers[x]}")

# function3()

def function4(): #using traditional method not for..in loops
    numbers = [1,2,3,4,5,6,7,8,9,10]
    positions = [0,1,2,3,4,5,6,7,8,9]
    for x in positions:
        print(f"Value = {numbers[x]}")

# function4()

def function5():

    #using range method 
#   it accepts 3 parametres (param1,param2,param3)
#    param1: start : where to start
#    param2: stop, where to stop(stop will always  executed )
#    param3: step count, how to generate the nexr value 
#    range(): used to create a sequence of numbers
    position = list(range(0,10,1)) # in case of 1 param3 is not exactly needed

    print(f"position: {position}")
    position = list(range(0,10,2)) # in case of 1 param3 is not exactly needed
    print(f"position: {position}")

# function5()

def function6():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    position = list(range(0,len(numbers)))
    print(f"Positions = {position}")

# function6()

def function7(): # doing this with no other positions collection which is aquiring memory space 
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for x in list(range(0,len(numbers))):
        print(f"value x  = {numbers[x]}")
    
    #in for loop we dont have to type or add list keyword
# function7()

def function8():
    number = 4
    if number % 2 == 0:
        print("It is even")
    else: print("It is odd")

# function8()

def function9():
    numbers = int(input("Enter a number"))
    is_prime = True
    for x in range(2,numbers): 
        # will create a flag to chekck if the number is prime or not
        if numbers % x == 0:
            print(f"remainder dividing {numbers} by {x} is = {numbers%x}")
            is_prime = False
            print("It is divisible")
            break


    if is_prime == True:
        print(f"{numbers} is PRIM")
    else: 
        print("It is not a prime number ")

# function9()


# pythonic method 

def function10():
    numbers = int(input("Enter a number"))
    for x in range(2,numbers): 
        # will create a flag to chekck if the number is prime or not
        if numbers % x == 0:
            print(f"remainder dividing {numbers} by {x} is = {numbers%x}")
            print("It is divisible")
            break

    else: print("It is prime number")
    
# function10()

# user input to entre numbers in list using for loop 
def function11():
    names = []
    numberofnames = int(input("Daaal be input"))
    for x in range(numberofnames):
        name = (input(":abe naam daal naam "))
        names.append(name)

    print(names)

# function11()

# indexing 
def function12():
    number = [10,20,30,40,50,60]
    print(f"the values at 0 = {number[0]}")
    print(f"the values at 1 = {number[1]}")
    print(f"the values at 2 = {number[2]}")
    print(f"the values at 3 = {number[3]}")
    print(f"the values at 4 = {number[4]}")
    print(f"the values at 5 = {number[5]}")

# function12()
# the above was the example of positive indexing 


#Slicing 

def function13():
    number = [10,20,30,40,50,60,70,80,90,100]
    numbers2 = []
    for index in range(2,7):
        numbers2.append(number[index])

    print(number)
    print(numbers2)
# function13()

def function14():
    number = [10,20,30,40,50,60,70,80,90,100]
    nums = number[2:6] # slicing method 
    print(nums)

# function14()

def function15():
      number = [10,20,30,40,50,60,70,80,90,100]
      print(f"numbers = {number}")
      numbers2 = [[1,2,3],[4,5,6],[7,8,9]]
      print(numbers2)
# function15()