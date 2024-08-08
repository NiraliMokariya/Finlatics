#%% using if statement : it takes one value and returs true or false
age=int(input("Enter your Age:"))
if age>=18:
    print("You're eligible to vote")
# %%  if else: checks two conditions
age=int(input("enter your age:"))
if age>=18:
    print("you're eligible to vote")
else:
    print("You're not eligible to vote")
# %% if elif else statement is used to execute multiple conditions
marks=int(input("Enter marks:"))
if marks>=90:
    print("Excellent")
elif marks>=70:
    print("G    ood job")
else:
    print("Need to improve") 
# %% neested if = if statement within if statement
age=19
marks='B'
if age>=18:
    if marks=='A':
        print("Great job")
    else:
        print("work hard")
else:
    print("you are npot 18 and hence not eligible")

# %% example 2
age=int(input("Enter your  age:"))
if age>=16:
    print("You are eligible for learners permit")
    if age>=18:
        print("You are eligible for drivers license")
    else:
        print("you are eligible for provisional driving")
else:
    print("You are not eligible for learners permit.") 

# %% now we use datatypes to check for conditions
dict1={'b':2,'a':1,'c':3}
dict2={'a':1,'b':2,'c':3}
if dict1 == dict2:
    print("Dicts are equal")
else:
    print("Dicts are unequal") 
# %% incase of tuples:
t1=(1,2,3)
t2=(1,2,3)
if t1 == t2:
    print("Tuples are equal")
else:
    print("tuples are not equal")
    
#if we change order of t1 to (2,1,3),tuples wouldnt be equal

# %% incase of lists also same
t1=[1,2,3]
t2=[2,1,3]
print(id(t1))
print(id(t2))
if t1 == t2:
    print("lists are equal")
else:
    print("lists are not equal")

# %% now lets take example of weekdays
day=input("Enter a day of the week:")
if day=="Sat" or day == "sun":
    print("It\'s a weekend")
else:
    print("Not a weekend")

# %% ternary operators is used to print if-else in same lineage
age = 20
eligibility ="eligible" if age>=18 else "not eligible"
print(eligibility)

# %%
score=39
result="pass" if score>=50 else "retake" if score>=40 else "fail"
print(result)
# %%
