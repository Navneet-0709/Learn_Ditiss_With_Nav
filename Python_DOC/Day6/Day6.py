def func1():
    list_num = [10,20,30,40,50,]
    print(f"List numbers  = {list_num}")
    tuple_num = 10,20,30,40,50
    print(f"tuple numbers  = {tuple_num}")
    numbers = {10,20,30,40,50} 
    print(f"set numbers  = {numbers}")
# func1()

def func3():
    list_num = [10,20,30,40,50,10,20,30,40,50,10,20,30,40,50]
    print(f"List numbers  = {list_num}")
    tuple_num = 10,20,30,40,50,10,20,30,40,50
    print(f"tuple numbers  = {tuple_num}")
    numbers = {10,20,30,40,50,10,20,30,40,50,10,20,30,40,50} 
    print(f"set numbers  = {numbers}")
# func3()

def func4():
    numbers = {10,20,30,40,50,10,20,30,40,50,10,20,30,40,50} 
    numbers.add(11)
    print(f"set numbers  = {numbers}")
# func4()

def func5():
    numbers = {10,20,30,40,50,10,20,30,40,50,10,20,30,40,50} 
    tuple_numbers = tuple(numbers)
    print(f"set numbers  = {numbers}")
    print(f"set numbers  = {tuple_numbers}")
    list1= list(numbers)
    print(f"set numbers  = {list1}")
    list1.sort()
    print(f"set numbers  = {list1}")
# func5()

def func6():
    numbers = {10,20,30,40,50,10,20,30,40,50,10,20,30,40,50} 
    numbers.discard(10)
    print(f"set numbers  = {numbers}")
# func6()

def func7():
    s1 = {10,20,30,40,50,100} 
    s2 = {40,50,610,70,80,90,100} 
    print(s1)
    print(s2)
    s3 = s1.union(s2)    
    print(s3)
# func7()

def func8():
    s1 = {10,20,30,40,50,100} 
    s2 = {40,50,610,70,80,90,100} 
    print(s1)
    print(s2)
    s3 = s1.intersection(s2)    
    print(s3)
# func8()

def func9():
    s1 = {10,20,30,40,50,100} 
    s2 = {40,50,60,70,80,90,100} 
    print(s1)
    print(s2)
    s3 = s1- s2
    s4 = s2 - s1
    print(s3)
    print(s4)
# func9()
# Dictionary 

def func10():
    person = {"name":"NAvneet","age":22,"add":"DEllllhi","Mail":"Navneet0709@gmail" }
    person2 = {"name":"MAnu","age":21,"add":"DEllllhi","Mail":"manu@gmail" }
    print(person)
    print(f"name = {person.keys()}")
    print(f"name = {person['name']}")
    print(f"name = {person.values()}")
    
func10()