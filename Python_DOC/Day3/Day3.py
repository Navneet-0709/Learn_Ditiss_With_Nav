## day3 ()
##program 1
#num = 200
#print(f"num = {num}, type = {type(num)}")
#
## funtion type nad value which refrence of its body memory
#
#def function():
#    print("Inside Function")
#
#function()
#print(f"function = {function}, type = {type(function)}")
#
##output
## num = 200, type = <class 'int'>
##function = <function function at 0x00000263F2739C60>, type = <class 'function'>
##here 0x00000263F2739C60 this is the memory location the body of the func is at
#num2 = num
#num = 300
#
#print(f"num = {num}, type = {type(num)}")
#print(f"num2 = {num2}, type = {type(num2)}")
#
#
#
##global and Local Scope Understanding 
#
#def function1():
#    print("Inside Function1")
#
#function1()
#
##since the function os global one it can be accessed anywhere in the programm
#
##def function2():
##    print("Inside Function 2")
#    
#    def function3():
#        print("Inside Function 3")




# COLLECTIONS
#LIST [
def function():
    numbers = []
    print(f"numbers = {numbers}")

    numbers.append(60)
    print(f"numbers = {numbers}")

function()