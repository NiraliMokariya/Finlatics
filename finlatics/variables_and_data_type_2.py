#%%
number23=23
print(type(number23))
# %%
numberhi='hi'
print(type(numberhi))
# %%
number2=2.22
print(type(number2))
# %%
number3=3+2j
print(type(number3))
# %% Indexing
#we use indexing to find a particular object name from the array
fav_player = ["Virat","Dhoni",'Maxi','chahal','Rohit']
print(fav_player[2])
# %% negative indexing
print(fav_player[-1])
# %%
print(fav_player[-3])
# %% 
fav_word="NPKUJAA"
print(fav_word[4])                #positive indexing
# %%
print(fav_word[-2])               #negative indexing
# %% indexing for dictionary
capitals={
    'India':'Delhi',
    'Turkey':'Istanbul',
    'Japan':'Tokyo'
}
capitals['India']
capitals['Turkey']
print(capitals['Japan'])
# %% Sets do not support indexing
fav_colour={"red","green","yellow"}
print(fav_colour[0])                  #it'll show error
# %%Slicing : it allows to extract a portion or a slice
fruits=['apple','banana','orange','pineapple','sapota']
subset = fruits[0:4]
print(subset)

# %% step size
# determines the step between elements
# syntax is
#subset=Iteration[start:stop:step]
numbers = [0,1,2,3,4,5,6,7,8,9]
subset= numbers[0:6:2]            #for even numbers
print(subset)
# %% odd number
numbers = [0,1,2,3,5,8,7]
subset= numbers[0:5:1]
print(subset)
# %% mutable and immutable list:
list=[0,1,2,3,4,5]
list[3]=99
print("the updatted list is:",list)
# %% mutable and immutable dictionary
student_marks={ 'student1':80,'student2':90,'student3':66}
student_marks['student1']=89
print("updated student_marks",student_marks)
# %% sets are mutable 
#tuples are the only one which are immutable
time=(1,2,3,4)
time[1]=7
print(time)
# %% integer and strings are immutable too

