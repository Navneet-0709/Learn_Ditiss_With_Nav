# Day 5

*Going on with Tuples once again 
*Tuple is also known as immutbale collection of Similar and dissimilar Values 

# Tuple()


* Now what is a tuple? Python’s default collection, which supports immutable sequence creation that can’t be
 edited, modified, or changed.
```
>>> t1 = "Hello", "Reva", "$0$"
>>> t1
('Hello', 'Reva', '$0$')
```
* A tuple can be created by specifying your elements seperated by comma. But remember in order to create a tuple with single element of tuple, you need to specify it along with a comma, something like this:
```
>>> t2 = 3
>>> type(t2)
<class 'int'>
>>> t3 = 4,
>>> type(t3)
<class 'tuple'>
```
* If you wanted to create a tuple with a single value, you need to understand that it will store that value as the type of object, meaning it will store the element as the variable.
```
>>> t1 = list(range(1,6,3)), list(range(5,10,3))
>>> t1
([1, 4], [5, 8])
```
* Even if you are converting a list into a tuple with single value, it will store it as `(“Tuple”,)`
* You can create a tuple using a tuple function, using `tuple()`, and can convert a sequence into a tuple. 

Note that you can’t do anything to a tuple, you can’t even call all the functions like lists. Tuples are immutable can’t be edited. Tuple do include few operation that can be performed on tuple. `count()` and `index()` are two such operation that can be performed in tuples.

# Tuple PAcking
    - A feature of Python used to collect multiple value into a single tuple 
    - e.g numbers = 10,20,30,40,50
    - any set of numbers or variables or values returning will be returd as a tuple
# Tuple Unpacking
    - is basically getting the elements of tuple without using  idexing or slicing method 
    - by creating individual variables 
    - make sure the number of variables are matching with number of values to unpack
    - but there is an exception also  " * " this will store rest of the values 
    - using tuple unpacking will help in 

* Using tuple you can return multiple values using tuples, because tuple is very popularly used for unpacking of values, meaning you can send or pass lots of values using tuple. The example below explains that the unpacking of elements happens even when you return multiple values, something like this, `mul, div, add, sub = function(77)`.
```
>>> t1
('Hello', 'Reva', '$0$')
>>> x, y, z = t1
>>> x
'Hello'
>>> y
'Reva'
>>> z
'$0$'
```
Remember that this behavious of unpacking of items can be done throughout python, not only in tuple. This can be done using lists, tuples, and other collections. You might get `ValueError` if you tried unpacking more or less variables than that are available in the sequence.

* Tuples do support indexing, as elements in the sequence can be taken by iindices.
* Tuple also support the same paradigm of slicing and indexing as that of the lists.

* Tuples ususally can be used as the best way of unpacking the values in quick and simplest way possible, because when you try to `print(person2.items())` you will get a list of tuples storing values normally tuples do.
```
>>> person2.items()

# funtional Programming

    Discussion started with functional programming features you can find in Day3.md
    and introduced how we can a function as a paramtre in another function 
     - function is considered as first class citizen
     - function can be passed to another function as an argument
     - function can be returned as a return value from another function



    - callback funtion is develope by someone but used by others
    - entry point functions of languages are basically callback functions 
    - the function which is passed as an argument to another function 
    - is said to be a call back function 

                ```- def dummy_function():
                     print(f"inside dummy_function")

                     def function1(param):
                        print(f"inside function1")
                        print(f"param = {param}, type = {type(param)}")

                        param()
                    



# Map() function
     - used to transform values from one to another state
     - returns a collection having new forms of old values from collecion parametrs 
     - returned collection must be having the same size as that of the parameter
     - the function/lambda must return a transformed value 
     - parameters
     - param1: reference to the function (which will be called 
             everytime in the iteration)
     - function could be a named function or a lambda
    - param2: collection which needs to be iterated    

# For Codes and more understanding please refer Day 5 Codes
    
# filter() Function 
    - used to filter the values
    - used to select the values based on a criteria
    - returns a collection whose size may not be equal to the original one
    - returns a collection with original values matching the criteria
    - it is mandatory to return True/False from the function/lambda
    - parameters
      - param1: reference to the function (which will be called 
        everytime in the iteration)
        - function could be a named function or a lambda
      - param2: collection which needs to be iterated

#  - Using map() and lambda function

If you want, you can use both in a versatile way. If you could see the code below, explains the best way the code can written in the most simplest way possible.

def Double_(num_list = [[1,2,3,4,4,5]]):
    
    double_ = lambda x: x*2                 # After lambda function, variable becomes function

    num_list = list(map(double_, num_list)) # Here `double_` is a function through which the list iterates, each element getting doubled

    print(f"The updated list => {num_list}") 
    # Output: The updated number list => [2, 4, 6, 8, 8, 10]

For example, you have an interable object that you want, if you could perform some kind of operation on the iterable object, you could easily use lambda function.

>>> operate_ = lambda x: (x//20) + 3
>>> num = map(operate_, range(40, 120, 20))
>>> num
<map object at 0x1014a5c00>    # this shows how num points to meory location until casted to type() == list
>>> list(num) 
[5, 6, 7, 8]
       


# NOTE :- For better Understading of Syntax and Code please refer Day5py
-----------











#IMP
What Is list 
What is Tuple 
What is the diff between list and tuple 
Why list is called as Muttable collection
How to create a Tuple with one value
what is a tuple packing 
