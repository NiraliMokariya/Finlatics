#%%

import matplotlib.pyplot as plt
data = [25,26,27,28,29,30,60]
print(min(data))
Q1 = (25/100)*8
result1 = data[int(Q1)-1]
print(result1)
Q2= (50/100)*8
result2 = data[int(Q2)-1]
print(result2)
Q3 = (75/100)*8
result3 = data[int(Q3)-1]
print(result3)
print(max(data))


IQR = result3-result1
print(IQR)


lower_fence = data[int(Q1)-1] - 1.5 * IQR
print(lower_fence)

upper_fence = data[int(Q3)-1] + 1.5*IQR
print(upper_fence)

plt.boxplot(data)
plt.ylabel("age")
plt.xlabel("x")
plt.show()
# %%
import matplotlib.pyplot as plt
data = [25,26,27,28,29,30,60]
plt.boxplot(data)
plt.show()
# %%
