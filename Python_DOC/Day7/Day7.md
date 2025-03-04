In dictionary It is not allowed to have list , tupple or collections as keys 
Only scaler values are the ones we can se to have as keys
Inner Dictionary can have its own local or inner keys same as the key in outer ones 
# Strings()
*what is string collection? String is collection of characters, can be declared using single, double, triple quotes in strings.
    
    - is considered as a primitive data type 
    - the value will be stord in the variable directly 
    - immutable collection : read only
    - Collection of Characters 

A doc string could be accessed using the delder __doc__method, that retrives doc strings within the function.
def function_body():
    """
    This is doc string
    """
    pass

print(f"Print doc string => {function_body.__doc__}")

# Output: 
Print doc string => 
    This is doc string
    
You can use lower() method to make string lowercase, and use upper() for the uppercase.
You can use strip() to remove the leading and trailing white spaces in the string. This can be used as shown in the below example:
>>> s1 = "............This Is A String. This is a string........."
>>> s1.strip('.')
'This Is A String. This is a string'
>>> # Removing the whitespaces by default
>>> s1 = "  This Is A String. This is a string.  "
>>> s1.strip()
Replace a sbstring with another string, using replace() method, accepts two arguemts, _old and _new, becaue it is case sensitive. So that means, replace() method is a case sensitve function. .Remember that it doesn’t make changes in the same string
>>> str_in = "I am going to buy an iPhone"
>>> str_in.replace("iPhone", "Samsung")
'I am going to buy an Samsung'
>>> str_in
'I am going to buy an iPhone'
split() methods is used that returns a two part of the string based on the split condition. split() by default returns a list of the string only
>>> store = str2.split('?')
>>> store
['https:googel.com/index.html', 'key=iPhone']
Strings supports indexing, slicing, and other operations like the list.
Now, importantly, know that if converted a string, which is collecction of characters, you will get the a list of all the characters in the string.
>>> store
['https:googel.com/index.html', 'key=iPhone']
>>> list(store[1])
['k', 'e', 'y', '=', 'i', 'P', 'h', 'o', 'n', 'e']
Say if you created a list of number, now you want to amalgamate all the elements in the list. You can use join(list_name) method.
>>> "*".join(store)
'https:googel.com/index.html*key=iPhone'
You can use join(list_name) in different styles, thus joining using any string, like ’-*-’.join(list_name).
You add character that is also called as left aligned and right aligned operation.
>>> print(f"|{str1:>11}|")
|      Apple|
You can also print floating point numbers, show positive symbols in the numbers using string formatting.
>>> num = 900
>>> print(f"|{num:+}|")
|+900|
>>> print(f"|{num:e}|")
|9.000000e+02|
>>> print(f"|{num:E}|")
|9.000000E+02|
>>> print(f"|{num:.3f}|")
|900.000|
You can also check or convert the numbers in different paradigm as converting into the hexadecimal, octal. This is exemplified below:
>>> print(f"|{num:n}|")
|900|
>>> print(f"|{num:o}|")
|1604|
>>> print(f"|{num:x}|")
|384|
f"|{num:x}|" can be used without print statement, inside the python interpreter, this doesn’t need you to use print statement only.

So how do you take a input in python? Python through interpreter or even in console will always accepts input as strings, until and unless you modify them to list, int or any other.

Python input can be taken as int
Membership operation works in lists, tuple, and sets.

There can be for …. else loop, where the else statement can be associated to the for loop, if you add a break statement then the else blocal will not execute as it will break out of the block and else  blocak will not execute.


# Python Modules and PAckages 