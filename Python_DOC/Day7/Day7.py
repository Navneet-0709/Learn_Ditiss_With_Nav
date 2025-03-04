# String 
def Funct():
    name = "Steve Jobs"
    print(f"Name = {name}")



    # convert in lower or upper
    print(f"Name in Lower Case = {name.lower()}")
    
    print(f"Name in Upper Case = {name.upper()}")

# Funct()

def Function1():
    # Split is for spliting the string 
    full_Name = "Navneet Arora"
    names = full_Name.split(" ")
    print(names)
    url = "https://google.co.in/index.html"
    seperated_url = url.split("/")
    print(seperated_url)
    # seperate the protocol (schema)(https), Domain Name(google.co.in) ,path name (index.html)

    # replace() funciton is used to replace any  
# Function1()

def Funtion2():
    Url= "https://google.com/index.html?first_name=steve$Lastname=jobs"
    new_url= Url.split("$")
    print(new_url)
Funtion2()