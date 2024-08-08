 #Operators are used to perform some specific tasks
#Ex: x+y ;here x and y are considered as operands and + is the operator.
#Arithmetic operators:
#%% Addition operator(+)
x=5
y=15
result=x+y
print(result)
# %% subtraction operator(-)
x=5
y=15
result=x-y
print(result)

# %% Multiplication operator(*)
x=2
y=5
result=x*y
print(result)

# %% division operator(/)
x=10
y=2
result=x/y
print(result)

#%% modulo operator (%)
x=1001
y=20
result=x%y
print(result)
# %%  floor division (//)-->quotient
a=10
b=5
result=a//b
print(result)

# %% exponential operator (**)
a=5
b=2
result=a**b
print(result)


# %% 2) Assignment operators
#=
x=5
print(x)
# %% compound assignment operator --> mixture of assignment operator with some mathematical operator
#+=
x=2
x+=3
print(x)

# %%  -=
w=2
w-=1
print(w)

# %% *=
w=2
w*=2
print(w)

# %%  /=
q=20
q/=2
print(q)

# %% %=
q=11
q%=2
print(q)

# %% //=
q=20
q//=10
print(q)

# %%  Logical operator
#3 types - AND,OR,NOT
#AND = returns true if both are true or else false
x=10
y=20
result=(x>20) and (y<10)
print(result)
# %%
#OR= returns true if either one is true
x=10
y=20
result=(x<11) or (y<1)
print(result)
# %%  NOT = returns the opposite condition of the right answe
x=10
result=not(x<9)
print(result)


# %% Identity operator  = is and is not
a=5
b=5
print(a is b)     #true
print(a is not b)  #false
print(id(a))    #print memory address of a
print(id(b))    #print memory address of b
# %% but incase of list,dictionary etc, is not and is works differently
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a is not b)

# %%
a=(1,2,3)
b=(1,2,3)
print(a is b)
print(a is not b)
# %%
a="hii"
b="hii"
print(a is b)
# %%
a=500
b=500
print(a is b)
# %%
# this is not thatttttt used. Use == everytime dw.
#%% Membership operator
#uses in and not_in
fav_fruits=["apple","mango",'kiwi']
print("apple" in fav_fruits)
print("watermelon" in fav_fruits)
# %%  not in 
fav_fruits=["apple","mango",'kiwi']
print("muskmelon" not in fav_fruits)
print("mango" not in fav_fruits)
# %%  PEDMAS rule : parentheses>exp>div=multiplication(left to right)>addition,subtraction(left to right)
result= 5+3*2-(8/4)**2
print(result)

# %%
2**3
# %%
2**3**2
# %%
2**2**2
#%%
2**3**3
# %% assigning multiple variable values
a,b,c=2,3,4
print(a)
print(b)
print(c)

# %% chained assignment
x=y=z=20
print(x,y,x)

# %% swwapping values
a="Nirali"
print(f"my name is {a}")
b="niru"
print(f"My pet name is {b}")
#swap a and b
a,b=b,a
print(f'My new name is {a} ')
print(f"My nee pet name is {b}")
# %% we can also use compound operators
x="hello "
x+="world"
print(x)

# %% assigning diff values
x=5
x=x+2*3
print(x)
# %% we can also modify lists
my_name=["Nirali"]
my_name+=["Mokariya"]
print(my_name)
# %% dictionary
my_dict={'a':1,'b':2}
my_dict["c"]=3
print(my_dict)
# %% relational op
x=5
y=10
z=20
print(x<y<z)

# %% example we neter a value between 18 and 30 and check if lies within
a=int(input("enter your value:"))
between=18<=a<30
print(f"is the value between 18 and 13?{between}")
# %% operators incase of strings
a='azple'
b="aunty"
print(a<b)    #here,a is same so second characters are compared that z>u
# %%
word="python1"
print('a'<word>'z')
# %% comparing if lists are equal
a=[1,2,3]
b=[1,2,3]
print(f"Are the lists equal?{a==b}")
# %% using > or <
a=[1,2,3]
b=[1,3,2]
print(a<b)
# %% and operator is evaluated first
a=25
b=15
c=5
print((a<b) or (b<c) and (c>0))

# %% not>and>or
x=True
y=False
z=True
print(x or not y and z)

# %% parentheses havehighest precedence
print(not(x or y))

# %% interns that is stores valies in same memory space only for -5 to 256
x=29392801
y=29392801
print(x is y)
print(id(x))
print(id(y))
# %% membership ie in and not in
sent = "java is so cool"
print("java" in sent)
print("Python" not in sent)
# %% list
fruits=["apple",'banana','grapes']
print("apple" in fruits)
print('apple' in fruits and 'kiwi' in fruits)
# %%
