#%%
import math
num=22
result = math.degrees(num)
print(result)



#%% only to import one particular function
from math import sqrt
num=22
print(sqrt(num))




# %% using * for importing everything
from math import *
num=22
result=sqrt(num)
circum=3*pi
print(num,result)
print(circum)

# %% 1d numpy creation
import numpy 
list = [1,2,3,4,5]
list_1d = numpy.array(list)
print(list_1d)
# %% another way for creating 1d array
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)



# %%2d
import numpy as np
my_2d_array = np.array([[1,2,3],[4,5,6]])
print(my_2d_array)


# %% creating 3D numpy array
import numpy as np
my_3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(my_3D)


# %% np of zeros
import numpy as np
zero_array = np.zeros((3,4))
print(zero_array)


# %% no of ones
import numpy as np
ones_array = np.ones((3,4))
print(ones_array)


# %% arithmetic operations
import numpy as np
arr1 = np.array([1,2,3,4,5])
#addition
result1 = arr1+10
print(result1)
#subtraction
result2 = arr1-2
print(result2)
#multiplication
result3=arr1*4
print(result3)
#division
result4=arr1/2
print(result4)

# %%indexing in 1D
import numpy as np
arr = np.array([10.20,30,40,50])
print(arr[2])
# %% indexing in 2d
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1,2])


# %% slicing for rows
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1,:])

# %% slicing for colums
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:,2])

# %%indexing in 3d
import numpy as np
my_3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(my_3D)
# print(my_3D[0])
# print(my_3D[0,0])
# print(my_3D[1,0])
print(my_3D[0,1,0])
print(my_3D[1,1,1])

# %%
import numpy as np
my_3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(my_3D)
print(my_3D[1])
print(my_3D[1,1])
print(my_3D[1,1,1])
# %%
import numpy as nd
n=(1,2,3,4,5)
r=np.array(n)
print(r)
# %%
import pandas as pd
data = [0,2,3,4,5]
my_series=pd.Series(data)
print(my_series)
print(type(my_series))
print(my_series[1])
# %% index by default is 0,1,2,3,4 so on.to change that
import pandas as pd
b=pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(b)
# %% creating dataframe
import pandas as pd
data = {'name':["alice","john","ashu","aish"],
         'age':[22,21,20,26],
         "gender":['f','m','m','f']
        }
df=pd.DataFrame(data,index=['a','b','c','d'])
print(df)


# %% matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[0,9,8,7,6]
plt.plot(x,y)
plt.show()

# %% to add labels
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[0,9,8,7,6]
plt.plot(x,y)
plt.xlabel("hehe")
plt.ylabel("baba")
plt.show()

# %% using bar plot
import matplotlib.pyplot as plt
name = ['aru','ashu','akshu']
age=[12,14,6]
plt.bar(name,age,color = "green")
plt.xlabel("name")
plt.ylabel("age")
plt.title("Cousins")
plt.show()


# %% histogram
import matplotlib.pyplot as ply
data = [10,1,2,3,4,5,12,28,27,29,19,78,392,234,123]
plt.hist(data,bins=7,color="orange",edgecolor="black")
plt.xlabel("hii")
plt.ylabel("hello")
plt.title("hist")
plt.show()


# %% seaborn 
# import seaborn as sns
