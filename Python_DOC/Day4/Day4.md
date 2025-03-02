# Day 4
# Yesterday we have started Collection now we will be. moving forward with other topics of collection.
    - Dictionary 
    - Tuple
    - Sets

# Day goes with the revison of list collection, that is a collection of sequence, apart form tuples and strings, lists is mutable, that means dynamically changed. Different types of functions that are available with the list sequence, such as `count()`, `copy()`, `sort()`, `reverse()`.    

String are not mutable, it can’t be changed. 

    - So how does indexing mechanism works in python? Indexing means getting the value from the list, when iterating over it. There are two types, positive and negative indexing. No language supports negative indexing. Idexing can be done using subscripting operator, meaning `[]` specifying a index. But there are few things:

* `IndexError` is the error that will occur if tried accesing index that is out of the list, mening if four elements exist in list, then can’t access `list[5]`.
* You’ll see an `TypeError: list indices must be integers or slices, not float` if you tried using `1.3` something like that in the subscript operator to access the list element.

# List


#   - usinf loops 
        - using for...in loops in list and performed various operations :- refer to codes
        - we use for loop always whenever we already know the number of the iterations 
        - it does give index value to the developer 
        - always starts with 0th position 


* In python you can control iteration using `for … in … ` loop, in order to :
```
>>> number = [0,1,2,3]
>>> for i in number:
...   print(i)       
...
0
1
2
3
```
* Remember that `i` is not iterating over the indices of the list, that means that when iterating using `for…. in ..` loop, you are directly accessing the index, you might create a sepreate list for the `number_index` list to access index. It doesn’t work like C/C++.
```
>>> for i in l1:
...   print(i)
... 
String
Stirng1
String3
```
* Because in `for … in ` loop, it directly access the individual object of the list, if is it string, integer, tuple, or list itself.
```
>>> for i in l1:
...   print(i)
... 
String
Stirng1
String3
```

# range

`range()` function accepts three arguments, start, stop (upperbound, meaning it will leave the last one), and step, where step is the value to generate the number, by default it is 1.

    - it generates generators
    - it always give us sequential number
    - range itself give us a generator with the help of which we dont need list keyword iinn for loop 
    - in range its not neccessary to enter start and step in case of 0 and 1 respectively 
    - so we can diret;y run a for loop on range
    - just by entring the range suppose range(10) this means it will work from 0 to 9 but 1 step at a time

* You should always use `range()` only as generator. Remember to use `range()` with the list function if you want to generate a list of numbers. This is exemplified below:
```
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(range(0,12))       
range(0, 12)
>>> numbers = list(range(10,101, 10))
>>> numbers
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]     
```
* Instead of creating a whole list you can just iterate over the range function and get the values.
* Python `range()` function iterates in uni-directional, bi-directional praadigm, meaning it iterate in forward and uni-directional way, however you might choose to iterate in opposite direction, in bi-directional way, as exemplified below:
```
>>> list(range(-100, 10, 20))
[-100, -80, -60, -40, -20, 0]
>>> list(range(100, -100, 50))
[]
>>> list(range(100, -100, -50))
[100, 50, 0, -50]
>>> numbers.extend(list(range(100, 1000, 30)))
>>> numbers
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 130, 160, 190, 220, 250, 280, 310, 340, 370, 400, 430, 460, 490, 520, 550, 580, 610, 640, 670, 700, 730, 760, 790, 820, 850, 880, 910, 940, 970]
```




# for else loop
    - here an else is associated with for loop 
    - and this methid is presented in python only 
    - the else block of for loop will be called only whenall the values from the collection are iterated without   any breaking the loop
    - if the for loop by any chance gets broken then the else block will not be executed

    * You can use negative index postion in python in lists.
* Last value of list can be accessed using `list_name[-i]`, where `i` starts from `1`. For any index, say `-i` the corresponding mathematical index is  `len(list) - i`.
```
>>> l1
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> l1[len(l1)-2]
17
>>> l1[-2]
17
```

``` * Refer the codes In Day4.py in the same Directory ```
    
# indexing and Slicing
    #indexing 
        - getting the values form the collection using the idex position 
        - types
            - Positive indexing - Normal indexing that we use to do from the starting 
                                - BAsically using positive index starting with zero to the length of collection -1
            - Negative indexing - in negative indexing we use to 
                                - always starts from right to left 
                                    psv indexes  0   1   2   3   4
                                    list -       10  20  30  40  50 
                                    ngv indexes -5  -4  -3  -2  -1
                                - it gets converted to the positive indexing by substracting it from length of the collection 
                                - starts from -1 to -length of the collection 

``` * Refer the codes In Day4.py in the same Directory ```


# the below is the example of positive indexing 

                    example   - def function12():
                                    number = [10,20,30,40,50,60]
                                    print(f"the values at 0 = {number[0]}")
                                    print(f"the values at 1 = {number[1]}")
                                    print(f"the values at 2 = {number[2]}")
                                    print(f"the values at 3 = {number[3]}")
                                    print(f"the values at 4 = {number[4]}")
                                    print(f"the values at 5 = {number[5]}")

                            function12()
``` * Refer the codes In Day4.py in the same Directory ```
            
# the below is the example of negative indexing 
                    example   - def function13():
                                    number = [10,20,30,40,50,60]
                                    print(f"the values at 0 = {number[-5]}")
                                    print(f"the values at 1 = {number[-4]}")
                                    print(f"the values at 2 = {number[-3]}")
                                    print(f"the values at 3 = {number[-2]}")
                                    print(f"the values at 4 = {number[-1]}")

                            function13()
``` * Refer the codes In Day4.py in the same Directory ```

#  These were just a basic example for basic understanding 


# Slicing 
    - slicing is nothing but selecting a part of a collection 
    - selection must be sequential 
    - use : seperated parametres to get the slicing work 
    - param1:- start : where to start
    - param2:- stop, where to stop(stop will always  executed )
    - param3:- step count, how to generate the nexr value
    - syntax:- nums[start:stop:step]
``` * Refer the codes In Day4.py in the same Directory ```

* Python also supports slicing of list, meaning you can get the sequential slices of the collection or sequence. The syntax is simple, specifying start and stop (the upperbound) sperated by semicolan.
```
>>> numbers
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> numbers[2:6]
[30, 40, 50, 60]
```
* You also think of it as using the range functionality as slicing. Slicing has few properties:
    * The default value of start is 0
    * The default value of last is last position
    * The default value of the next count is 1
```
>>> numbers[:]               # list all the elements in the list
>>> numbers[1:len(numbers)]  # retuns the same list
>>> numbers[::-1]            # list all values in reverse order
```

# multi dimentional collections
    - multidimentional lisr
    - list of list 

    def function15():
      number = [10,20,30,40,50,60,70,80,90,100]
      print(f"numbers = {number}")

What is multi-dimensional collections? Meaning collection of collections or multipl dimension of collections. It is something like list of lists, tuple of tuples, list of tuples, tuple of lists.

* Until now we looked at lists, which were single dimensinal lists, but list of lists like like something like this:
```
>>> number
[[1,2,3], 
 [1,2,3], 
 [1,2,3]]
```
* When you create multiple lists in a list, individual list is seen as the single object, every position points to an object, say list, all of them can be accessed and the very object within the list carries the address of the object stored in the memory, can be accessed using index, say `number[1][0]` will return `1` of first element of second row.
* Remember that every single object, will be treated a seperate object (in our case, a single list).
```
>>> number
[[1, 2], [1, 2, 3]]
>>> for i in number:
...   print(i[0])
... 
1
1
>>> # Similar to lists tuples supports the same operation
>>> t1 = tuple(range(1,6,3)), tuple(range(5,10,3))
>>> t1
((1, 4), (5, 8))
```
* There is no restriction on lists, they can adopt any number of lists or any size. Because it is mutable, you can do any kind of operation on the lists, in fact on every object of the sequence. If you need to make changes within a list, you need to first reach to the object (in our case, the list within the list), as you will require to reach the list itself, `number[0].pop(2)` then you could perform list operation.

Remember you can add, edit, remove, and modify the list, even if it exist within a tuple, you can make changes in the list within a tuple but can’t make change in tuple, though removing all the element of the list will work, but the list can’t go off the tuple, because individual element of the sequence

* Remember that immutable objects are always faster than mutable objects, because the mutable objects needs to keep the track of changes. Few of the differences between list and tuple can be stated:
    * list uses linked list to store the values
    * tuple uses flat list to store values
    * list is slower as it has to traverse through the linked list to get the value
    * tuple  is faster as it can directly jump to location
    * the values in list aren’t stored contigeuosly, yes the values, not inside the memory, meaning when python stores the values of lists, say `my_list = [“hello”, “reva”, 404, [“hello”, “mrdhvi”, 402]]`, each value or say each object is stored in sequence, but inside the memory, there are pointers to these objects stored in contigeous memory.
    * and, tuples values are stored contigeously 
* The main thing is that tuple uses the metadata of the data, as when called it directly takes the data from the memory and return to you.


``` * Refer the codes In Day4.py in the same Directory ```



 # *NOTE All the notes will be available in Day4.py Please have a look 
 # and contact in case on any query
