#%%
name="John"
for a in name:
    print(a)
# %% range function (step size is a subset of range)
# range(start,stop,step)
for a in range(1,20,2):
    print(a)
# %% while loop
count=2
while count<=5:
    print("eating a cookie")
    count=count+1
    

# %% break
for i in range(1,29):
    print(i)
    if i == 19:
        print("this is it")
        break
    

# %% continue
for i in range(1,17):
    if i==7:
        print("this has been skipped")
        continue
    print(i)

# %% nested loop
for column in range(1,4):   #outer loop
    for row in range(1,4):  #inner loop
        print(f" ({column},{row})")

# %% next video on for
# user inputs code to give multiplication of integer
a=int(input("Enter your number:"))
print(f"The table for {a} would be")
for i in range(1,11):
    result = a * i
    print(f"{a} * {i} = {result}")
# %% if we want for odd number from 1 to 10
a=int(input("Enter your number:"))
print(f"The table for {a} would be")
for i in range(1,11,2):
    result = a * i
    print(f"{a} * {i} = {result}")

# %% multiplication tabel in reverse
a=int(input("Enter your number:"))
print(f"The table for {a} would be")
for i in range(10,0,-2):
    result = i*a
    print(f"{a} * {i} = {result}")

# %% calculating sum of numbers from 0 to 10
a = 0
for i in range(1,11):
    a+=i
print(a)


# %% 
a = 0
prev_a = 0
for i in range(0,6):
    prev_a = a
    a+= i
    print(f"Current value of i : {i} and current value of a : {a} which is {prev_a}+{a}")
print(f"sum of first 5 numbers is :{a}")

# %%  user to enter a value and lets calc sum of numbers upto that value
a=int(input("Enter a number:"))
sum_result = 0
#calculate the sum of numbers upto the user-entered value
for i in range(0,a+1):
    sum_result += i
print(f"sum of numbers from 0 to {a} is: {sum_result}")

# %% print every element of a list
a=['mango','orange','kiwi','banana','grapes']
for i in a:
    print(i)

# %% key value pairs of a dict
student_marks = {"ash":92,"harshu":93,"aishu":97,"jaaaannavi":96}
for i in student_marks:
    print("student:",i,"marks:",student_marks[i])

# %% access ash marks
student_marks = {"ash":92,"harshu":93,"aishu":97,"jaaaannavi":96}
# for i in student_marks:
    # print("student:",i,"marks:",student_marks[i])
ash_marks=student_marks["ash"]
print("Ash marks=",ash_marks)

# %% negative integers from -1 to-5
for i in range(-1,-6,-1):
    print(i)

# %% len function
# used to find the length or the number of ele in list or tuple..
x="hello"
print(len(x))

# %% reverse a list
list=["apple",'mango','orange','cherry']
# print(len(list))
for i in range(len(list)-1,-1,-1):
     print(list[i])
# %%

print(*list[::-1],sep='\n')

# %% using while loop
a = ['m','n','o','p']
i=len(a)-1
while i>=0:
    print(a[i])
    i-=1

# %%
a = ['m','n','o','p']
num=int(input("enter the number of fruits to be printed:"))
i=0
while i<=num-1:
    print(a[i])
    i+=1

# %% to check if a number is present and tocheck if its een or odd
a=[2,22,11,13,15,18,20]
b=int(input("enter your number to check:"))
if b in a:
    print(f"{b} is present in a")
    # to check if its odd or even
    if b % 2 == 0:
        print(f"{b} is even")
    else:
        print(f"{b} is odd")
else:
    print(f"{b} is not present in a")

# %%  list of colors that iterates and prints each color along with individual character
colors=["red",'green','blue','yellow','orange']
for color in colors:
    print(color)
    # for char in color:
    #     print(char)

# %% give grades to students
score = [90,91,12,15,77,76,82]
for i in score:
    print(f"score:{i}")
    if i>=90:
        print("Grade:A")
    elif 80<=i<90:
        print("Grade:B")
    elif 70<=i<80:
        print("Grade:c")
    else:
        print("Grade:F")
    print("---------------------")

# %%  login system where user enters a username and passowrd
# has three attempts to enter right credentials
correct_username = "nirali"
correct_pass = "nirali123"
attempts = 0
max_attempts = 3
while attempts<max_attempts:
    username=input("Enter username")
    password=input("enter password")
    
    if username == correct_username and password == correct_pass:
        print("Login successful")
        break
    else:
        print("wrong pass")
    
    attempts+=1
if attempts == max_attempts:
    print("Sorry,youve rrached max no of attempts.acc lo")
#doubt
# %% print the smallest number in list

my_list = [5,3,8,0]
smallest = my_list[0]

for num in my_list:

    if num<smallest:
        smallest=num

print("The smallest value in list is",smallest)

# %%
a=[5,1,2,0]
a.sort()
# print(*a)
print("The smallest value is:",a[0])
# %%
