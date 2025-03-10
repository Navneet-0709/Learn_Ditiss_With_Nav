# Day 6
*Revision of List Comprehension 
* Always try to use tuple rather than list in moat of the cases 
* on case u want to chaneg or modify the collection then ofc we have to use list

# Set 

So what is a set? Set is a collection of unique elements stored in unordered items, meaning when you define a set, the items within it aren’t stored in sequence. Though set is a collection. 
```
>>> s1 = {"Hello", "World", 21, 2, 21, 2, 'Hello'} # collection of similar and dissimilar values
>>> s1
{'World', 2, 'Hello', 21}
```
- Mutable collection so unique, similar or dissimilar values
- can be created using curly brackets 
- {} it is used for both Dictionary and Set 
-  you cannot create an emoty set by just set  = {}
    as it will be creating a dictionary 
- we can create empty set only by using set()
- set is not an ordered collection (Does not maintain any kind of insertion order )
- set() is one of the type of type coversion function 
-  since the set uses hash function behind the scene to decide the position of a value, or the insertion ordr of the elements will never maintained 
- set object is not subscriptable (cannot be accessed the lements using any indexing or other methods )
- because of that we will not be able to add anything at the end or in between 
- either we can access all the values useing for in loop 
- or we can only access it by converting the sets into tuple or list 
// - in general
Hash Function - are one who decide the index in set function,  will always return the same value for a particular input  
// 
    Operations on Set():-
        - add ()
        to add any value in the set irrespective or positions or indexing 
        
        - discard ()
        to remove the value from the set 

        -intersection()
        to find the common values between two sets 
        here s1 intersection s2 and s2 intersection s1 will be same 

        -union()
        to create a new set containing a unique set of all the values in both sets 
        here s1 union s2 and s2 union s1 will be same 
        keeping all the common elements only once

        -Substraction operation()
        finding out un commonn values of the set 
        here s1 - s2 and s2 - s1 will not be same 
```
s1 = {[1,2,3], [1,2,3]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'>>> s1 = {[1,2,3], [1,2,3]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
* It will give you an unhasable type. Only mutable objects can’t be part of sets, like lists, because hashable type for different types is different, but it can’t do the different datatype hashing at the same time.  
* Sets can be also immutable, called frozen sets, using `frozenset()` function, then any other element can’t be edited or added any other.

# Frozen Set 
    - itself a set but an immutable one 
    - immutable collection of unique values 

# Dictionary  
    - Colections of Key-Vlaue Pairs
    - can be create dusing {}
    
Let’s get into Dictionary? Dictionary is one the way that dictionary can store a meaningful data. This is because, dictionary uses key:value pair, each dictionary is accessed using the key that it can be edited, modified. 

When creating a dictionary, you need to consider creating key as string only, it can be through of different data type but you can create dictionary with different values.

* You can access the keys using syntax `d.keys()` and get the values using `d.values()`.
* Remember that lists are solely dependent on the indices, but the dictionaries are only dependent on the keys.

* You can’t store element or information of person in `sets`
* Therefore, you need to use lists.
* If you can see in `inner_fun()` where we are printing the information of the dictionary, the elements of the dictionary was accessed using the key, because it allows you to directly access the values using keys.
```
def fun1():
    # creating person info*
    person = {
        "name": "Reva", 
        "age": 22, 
        "place": "pune"
        }

    def inner_fun(person):
        # printing person info*
        print(f"name => {person['name']}")
        print(f"age => {person['age']}")
        print(f"place => {person['place']}")

# Output:
name => Reva
age => 22
place => pune
```
If while accessing the keys of the dictionary, you use double quotes person[“key”], you might get an error, because that will be caused due to the improper use of double quotes, you need to use single quotes like mentioned in above snippet.

* Never prefer sequence for passing the elements as arguments if you don’t want any changes to occur, use tuple.
* You can define a dictionary in such as way:
```
# way 1
person1 = {"name": "reva", "age": 18, "address": "pune"}

#way 2
# create an empty 
car = {}
# add key:value pairs
car['color'] = "lmn"
car['color2'] = "xyz"
car['color3'] = "abc"

```
* Remember, there always will be one one key with one value, even if you tried making a key with same value, then you see your previous key getting overirde with the new value.

It is recommended that you only use the string value as the key, though you can also use the one with otherkind of sequences, but a convention to use only string type as keys while defining a dictionary. 
You can use `”color”: None` to define key:value pair, 

* In the below snapshot, you can’t leave a string after a comma, because it’ll expect a value for the respective key.
```
>>> # There can be any data type within a dictionary
>>> person2 = {"name": "reva", "age": 18, "address": ("agra", "284001")}
```
* In dictionary you can remove the element in the dictionary using `del` statement. In order to remove the element in the dictionary you need to know the key, you can’t remove the element without it. 
```
>>> del person2["age"]
>>> person2
{'name': 'reva', 'address': ('agra', '284001'), 'key': (1, 2, 23)}
```
* If you using `person2["hobbies"]` where hobbies doesn’t exists, the you’ll get a key error, but in `get()` method it doesn’t crashes, it will return None, instead of raising an error, because most of times, you don’t know what keys are present in dictionary, if you are not damm sure, you don’t use square brackets, then you use `get()` method. This is also exemplified in below example:
```
>>> person2["name"]
'reva'
>>> person2.get('name')
'reva'
>>> person2["hobbies"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'hobbies'
>>> person2.get("hobbies")
>>> # It executes without any issue
```
* When iterating over the dictionary, never assign a key in double quotes because key is the key of the dictionary itself, not the value of key, meaning when you are iterating over `person2`, then you can simple use key to refer keys of the dictionary `person2`. Don’t use `person2[“key”]`, which is syntactically wrong.
```
>>> for key in person2:
...   print(f"{key}: {person2[key]}")
... 
name: reva
address: ('agra', '284001')
key: (1, 2, 23)
```
* You can use tuple unpacking in the eaiest way possible, even when you want them to run within a `for` loop. This is exemplified below:
```
# Create a list of tuple
l1 = [
        ("reva", 22, "address"),
        ("reva", 23, "address"),
        ("reva", 24, "address")
    ]
# A better way to print at once
for name, age, address in l1:
        print(f"name: {name}")
        print(f"name: {age}")
        print(f"name: {address}")

```
* Tuples ususally can be used as the best way of unpacking the values in quick and simplest way possible, because when you try to `print(person2.items())` you will get a list of tuples storing values normally tuples do.
```
>>> person2.items()
dict_items([('name', 'reva'), ('address', ('agra', '284001')), ('key', (1, 2, 23))])
```
* A list of tuples containg two values in (‘key’, ‘value’) paradigm. This allows easy access of the values in the tuples, as they an unpacked at ease. This is exemplified below:
```
def function1():
    # Printing a dictionary content using `items()` methods.
    d1_person = {
        "name": "reva",
        "age": 22, 
        "place": "pune", 
        "hobbies": "reading and writing"
    }

    print(d1_person.items())
    print()
    for key, values in d1_person.items():
        print(f"{key}: {values}")
```
* How dictionaries get stored in memory? Behind the scene it stores two collection are created, all the keys will be stored in one collection, then it get managed by another collection, that is why you can store them as an individual callection.

Remember that when using `item()` methods it is only giving the copy of dictionary in the format of list of tuples. It has nothing to do with the dictionary itself. Not even it is a restriction on the dictionary that it become immutable because the dictionary values are getting accessed using tuples. It is just the copy of values of dictionary. 

* If you looking for adding multiple values(parameters) to the function, you can do that using variable length arguments. 
    * To create a VLA, you can use `*` before the argument, such as `def function(*args, **kwargs)` where a single `* ` denotes positional arguments, and `**` denotes keyword arguments or say named arguments.
    * `*args` says that you can pass end number of parameter to it, which are stored as tuples of values you pass. Similarly, `**kwargs` says that it can store all the keyword arguments, which are stored as dictionaries, as keys: values pairs.
```
def outer_fun5(*args):           # '*' makes the arguments of variable length
    print(f"args => {args}, type => {type(args)}")

outer_fun5(23,23,2,3,{1,2,3,3},2,(1,2,3,4),21) # passing variable lenght arguments

output: args => (23, 23, 2, 3, {1, 2, 3}, 2, (1, 2, 3, 4), 21), type => <class 'tuple'>
```
Every time a function is create there will be a function activation record, but remember that symbol table isn’t the same, as a function activation table is executed during the compilation, and symbol table is executed during the runtime of the compiler (or python).

* If you want to pass the variable length keyword arguments, you can go with `**keyword_args`, remember that all the positional arguments needs to come before the keyword arguments. The example for the keyword arguments is exemplified below:
```
# keywords arguments
def outer_fun6(**keywords_args):
    print("Inside the outer_fun6")
    print(f"args => {keywords_args}, type => {type(keywords_args)}")

outer_fun6(k1 = 20, k2 = (1,2,3,4), k3 = ["hello", "reva"], k4 = {"one": 1, "two": 2})

# output:
Inside the outer_fun6
args => {'k1': 20, 'k2': (1, 2, 3, 4), 'k3': ['hello', 'reva'], 'k4': {'one': 1, 'two': 2}}, type => <class 'dict'>
```
* As you can see that when you print all the keyword argments, they got printed as dictionaries as key:value pairs along with keywords as keys.
