#%%
def add(a,b):
    sum = a+b
    return sum
a=2
b=3
result = add(a,b)
print("the sum is:",result)
# %%
def say_hello():
    print("Hello,there!")
    print("Hello,there!")
    print("Hello,there!")
    print("Hello,there!")
    print("Hello,there!")
    

# %%
say_hello()
say_hello()

# %%

a=int(input("Enter your value"))
b=a**2
print("the sqyare is:",b)


# %%default argument ex
def greet(name,greeting = "Hello"):
    print(f"{greeting},{name}")
    
#using the function without providing a greeting
greet("Bob")

# using the function with a custom greeting
greet('alice','Hii')

# %%Positional argument
def add(x,y):
    result = x+y
    return result
result = add(3,5)
print(result)

# %%keyword argument
def sub(x,y):
    result=x-y
    return result
result_pos = sub(5,3)
print(result_pos)     # this is positional argument
result = sub(y=2,x=3)
print(result)         
# %%arbitraty argument (*args)
# ex of pizza where customer can add any number of toppongd
def make_pizza(*toppings):
    print("making pizzas with following toppings")
    for topping in toppings:
        print("-",topping)

#ordering pizza
make_pizza("Cheese","Pepperoni")
make_pizza("mushroom","Onions","Bell peppers")
make_pizza("sausage","green olives","Tomatoes")

# %% varible length keyword arguments
# allows a function to accept an abitrary number of keyword arguments
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

#process each key-value pair as needed
print_info(name='john',age=25,city='delhi',occupation="doctor")


# %% lambda function
#to create anonymous or unnamed function
# used for short lived function
def square(x):
    return x**2
print(square(5))

# %% now the same example using lambda function
sq=lambda x:x**2
result=sq(5)
print(result)




# %% next lec
float_value = 5.7
integer = int(float_value)
print(integer)

# %%
complex_number = complex(*2,5)
print(complex_number)
# %% pow() function
result=pow(3,2)
print(result)

# %% round function - rounding to nearesr integers
float_num = 3.4
print(round(float_num))

# %% len function
a="string"
print(len(a))
# %% min() and max()
a=[1,2,1,2,3,0,4,5,6,2,1,7,8,3]
print(min(a))
print(max(a))
# %% sum() function
a=[1,2,3,4,4]
b={1,2,3,1}
c=(1,2,3,1,4)
print(f"the sum of a is : ",sum(a),"the sum of b is :",sum(b),"the sum of c is:",sum(c),sep="\n")

# %% count()
a=[1,2,3,1,2,5]
print(a.count(1))
# %% upper() and lower()
a="Hello"
print(a.upper())
print(a.lower())

# %%capitalize()
a="hello"
print(a.capitalize())

# %% title()
a="python is a versatile programming lan"
print(a.title())

# %% replace()
a='python is good and fine'
print(a.replace("good","bad",2))

# %% to find index,we use find()
a="python is a powerful is language"
print(a.find("t"))

# %% split()
a="python is cool"
print(*a.split())

# %% another example for split()
a=input("Your desired year (dd-mm-yyyy):")
day,month,year=a.split("-")
print("Day:",day)
print("month:",month)
print("year:",year)
# %% using maxsplit in split()
a="pythoon;is;a;good;lang."
print(a.split(":"))

# %% startswith() and endswith()
a="document.txt"
if a.startswith("document"):
     print("document type")
elif a.startswith("image"):
    print("its an image type")
else:
    print("unknown")

# %% endswith function
a=input("Enter you email:")
if a.endswith(".com"):
    print("This is a valid mail id")
else:
    print("Invalid")

# %% example of urls
a=("http://","https://","ftp://")
user_input = input("enter your url:")
if user_input.startswith(a):
    print("the URL is valid")
else:
    print("The url is invalid")

# %% strip()
a="    python"
print(a.strip())


# %% another example
user_names = ["  john", "asma ","   sunain    ", "ayesha "]
cleaned_names = [name.strip() for name in user_names]
print("Original names:", user_names)
print("cleaned_names:", cleaned_names)
# %% same question different approach
user_names = ["  john", "asma ","   sunain    ", "ayesha "]
cleaned_names = []
for name in user_names:
    cleaned_names.append(name.strip())
print("Original names:",user_names)
print("Cleaned_names:",cleaned_names)

# %% fucntions ussed in lists
#append
a=[]
for i in range(3):
    movie = input("enter your fav movies:")
    a.append(movie)
print("Your fav movies:",a)

# %% extend()
a=["a","b","c","d"]
print("The first list is:",a)
b=['A','B','C','D']
print("The second list is:",b)
a.extend(b)
print("The extended list is",*a)

# %% insert()
a=[1,2,3,4]
print("Current a is:",a)
a.insert(1,10)
print(a)

# %% reverse()
a=[54,4,3,2,1]
a.reverse()
print(a)
# %% sort()
a=[5,2,8,1,3]
a.sort()
print(a)

# %% to sort in desc order
a=[5,2,8,1,3]
a.sort(reverse=True)
print(a)

# %%remove
a=[5,2,8,1,3]
a.remove(4)
print(a)

# %% index
a=[5,2,8,1,3]
print(a.index(3))

# %% any()
a=[False,False,False,False]
print(any(a))

# %%all
a=[True,True]
print(all(a))

# %% using any and all
temperature = [25,30,28,32,29]
for_any=any(temp>30 for temp in temperature)
for_all=all(temp>30 for temp in temperature)

if for_any:
    print("at least one temperature is above 30 degree celsius")
else:
    print("no temp is above 30 degree celsius")
if for_all:
    print("All the temp are above 30 degree celsius")
else:
    print("not all temp are above 30 degree celsius")



#%% just like how we use append in lists,we use add in sets
cart = {"apple","banana","orange"}
item_to_add=input("the item to be added is:")
cart.add(item_to_add)
print("the cart has follows:",cart)
# %%
a={2,1,1,3}
print(a)
# %% discard() and remove()
a={"banana","orange","apple"}
print(a.remove("grapes"))

# %% hence we use discard function
a={"banana","orange","apple"}
a.discard("grapes")
print(a)
# %% union and intersection
a={1,2,3}
b={4,5}
c=a.union(b)
print("Union is:",c)
d=a.intersection(b)
print("intersection is :",d)
# %% key() and value()
info = {"name":"nirali",
        "age":23,
        "place":"pune"}
# to retrieve keys()
print("the keys are:",info.keys())
print("the values are:",info.values())
print("the items are:",info.items())   # to get both key value pair together
#to add extra pair value:
info["state"]="maharashtra"
print(info)

# we can also use update() to add extra pairs or to update the existing pairs
info.update({"height":"156cm"})
print(info)
info.update({"age":"20"})
print(info)

#get() to retrieve something from dict
# info.get("age")
info.get("status")
# %%pop
a=(1,2,3,4,5)
a.pop()
print(a)
# %% pop used in dict
a={'a':1,'b': 2,'c':3}
a.pop("b")
print(a)

# %% if value not present
a={'a':1,'b': 2,'c':3}
# a.pop("d")
# print(a)  # this would give error hence we use
a.pop('d',0)    #here d is key and 0 is default
print(a)



# %% understandings from yt 
def greet():
    print("Hii")
    
    
greet()
# %%
def greet(x,y):
    print("Hello",x,y)
greet("nish","woman")
# greet("ash")    # here it would give error because theres only one argument given
greet("ash","heb")


# %% there are two types of function : 1) perform a task. eg:print("hii") 2)return a value  eg:round(0.9)
# difference between the two with an example

def greet(name):
    print(f"hi,{name}")
greet("nirali")

# %% whereas,return function:
def greet(name):
    return f"Hello,{name}"

greet("nirali")

# %%
def greet(name):
    return f"Hello,{name}"

message = greet("nirali")
print(message)

# file = open("Project 1,doc","w")
# file.write(message)

# %% 
def increment(number,by):
    return number+by

print(increment(2,1))

# %% to make it more readable,we use keyword
def increment(number,by):
    return number+by

print(increment(2,by=1))

# %% 
def increment(number,by=1):    # here if we do not give any value for by later,it takes 1 by dafault
    return number+by

print(increment(2))

# %%
def increment(number,by=1):
    return number+by

print(increment(2,5))

# %%  *
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,10))

# %% **
def save_user(**user):
    print(user)
save_user(id=1,name="john",age=22)


# %%
def save_user(**user):
    print(user['age'])
save_user(id=1,name="john",age=22)


# %% to find factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        facto = n*factorial(n-1)
        return facto
result = factorial(0)
print("The factorial of 6 is:",result)

# %%
def sum_of_digits(x,y,z):
    print("The sum of digits is:")
    return x+y+z
output = sum_of_digits(4,5,6)
print(output)

    
# %%
def sum_of_digits(n):
    if n<10:
        return n
    else:
        a = (n%10)+(sum_of_digits(n//10))
    return a
num= int(input("enter your number:\n"))
result = sum_of_digits(num)
print(f"the sum of digits in {num} is", result)

# %% countdown from some number to 1
def countdown(n):
    if n<=0:
        print("Happy new year")
    else:
        print(n)
        countdown(n-1)
num = int(input("enter your number:"))
countdown(num)
# %%
