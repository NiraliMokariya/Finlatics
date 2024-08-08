#%% Write a Python program that takes user input for their name and greets the user. Then, prompt the user to enter two values. After receiving the values, swap them and print both the original values and the swapped values.
name=input("Enter your name:")
print(f"welcome to the club , {name}")
value1=int(input("Print the first value:"))
value2=int(input("Print the second value:"))
print(f"The original value1 is:{value1}")
print(f"The original value2 is:{value2}")
#after swapping
value1,value2=value2,value1
print(f"The swapped value1:{value1}")
print(f"The swapped value2:{value2}")

# %% Write a Python program that asks the user to input the radius of a circle. Calculate the area of the circle using the formula area = π * radius^2, where π (pi) is a constant approximately equal to 3.14. Print out the calculated area. Ensure that the user input for the radius is converted to a float data type before performing calculations.
circumference = float(input("The circumference of a circle is:"))
pi = 3.14
radius = circumference/(2*pi)                    
print(radius)
#area of a circe = pi*r^2
area = pi*radius**2
print(area)

# %% Write a Python program where the user is prompted to input their birth year. The program should then calculate and display the user's current age.
birth_year = int(input("Enter your birth year :"))
print(f"Your age is {2024-birth_year}")

# %% Write a Python program where customers are prompted to input their name and favorite cake flavor. The program should then print a customized message saying: "Hello, [name]! We're delighted to serve you your favorite [favorite_cake] cake on your birthday. Happy Birthday."
name = input("Enter your name:")
fav_cake = input("Enter your fav cake flavor:")
print(f"Hello, {name}! We're delighted to serve you your favorite {fav_cake} cake on your birthday. Happy Birthday.")

# %% Write a Python program to calculate the simple interest with user input for principal amount, rate, and time.
principal = float(input("Enter principal value:"))
rate = float(input("Enter Rate of interest:"))
time = int(input("Enter time:"))
si = (principal*rate*time)/100
print(si)
# %%
