#%%
'''Q1) Write a Python program to initialize a 3x3 NumPy array with any integer values of your choice. Then, perform the following operations:
Multiply the entire array by 2.
Add 5 to each element of the array.
Calculate the square of each element in the array.
Print the original array and the results of each operation.'''

import numpy as np
my_array = np.array([[1,2,3],[4,5,2],[2,1,8]])
print("My array is:",my_array,sep='\n')
result1 = my_array * 2
print("The result after multiplying each element by 2 is:",result1,sep = '\n')
result2 = my_array+5
print("The result after adding 5 to each element is:",result2,sep='\n')
result3 = my_array**2
print("The square of each element is :",result3,sep="\n")
print("The original array is:",my_array,sep='\n')
print("result1:",result1,sep='\n')
print("result2:",result2,sep='\n')
print('result3:',result3,sep='\n')


# %%
'''Q2) Write a Python program to initialize a 3x3 NumPy array with any integer values of your choice. Then, perform the following slicing operations:
Extract the first row of the array.
Extract the last column of the array.
Extract a 2x2 sub-array from the center of the original array.'''

import numpy as np
arr = np.array([[1,2,4],[8,9,5],[6,5,0]])
print("result1:",arr[0,:])
print("result2:",arr[:,2])
print("result3:",arr[1:3,1:3],sep='\n')


# %%
'''Q3) Write a program to create a DataFrame in Python to store the names and marks of 10 students. Each row of the DataFrame should represent a student, with columns as 'Name' and 'Marks'. Populate the DataFrame with appropriate data and then print it.'''

import pandas as pd
data = {
    "name":["Aradhya","Abhishek","Avinash","Ashwin","Ashwini","Aish","Janavi","Krupali","Uday","Kailash"],
    "marks": [90,80,99,78,62,70,66,99,95,92]
        }
df = pd.DataFrame(data,index=[1,2,3,4,5,6,7,8,9,10])
print(df)


# %%
'''Q4) Write a python program to create a DataFrame representing the names and income of 5 employees. The DataFrame should include columns ' Employee_name’ and ‘Income', and each row should correspond to an individual employee. Use the indices 'a', 'b', 'c', 'd', and 'e' for the DataFrame entries to uniquely identify each employee.'''

import pandas as ppd
data = {
    "Employee_name":["Ashwini","Abhishek","Janavi","Sid","Mala"],
    "Income" : [30000,40000,30000,27000,10000]}
df = pd.DataFrame(data,index=["a","b","c","d","e"])
print(df)


# %%
'''Q5) Imagine you're tasked with visualizing data using Python. You have the following dataset representing the frequency of occurrences for categories A, B, C, D, and E, stored in two lists:
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]
Write a Python script that creates a bar plot to visualize this data. The categories A, B, C, D, and E should be displayed on the x-axis, while the corresponding frequencies should be displayed on the y-axis.'''

import matplotlib.pyplot as plt
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]
plt.bar(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bar Graph")
plt.show()

