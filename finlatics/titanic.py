#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading dataset
# df = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\titanic.csv')

#for loading using sns
df = sns.load_dataset('titanic')


pd.set_option("display.max_rows",None)          # use of some number instead of none would give so many rows. we if take 6 instead of none,we would get first three attributes and last three attributes
pd.set_option("display.max_columns",None)       #here,none represents,none cols should be excluded basically

# print(df.head(10))    # head gives first 5 values by default if we use ()

# print(df.tail(10))    # here tail gives last 5 values by default if we use () 

# print(df.info())        # gives important details about the dataset including the rangeindex

# print(df.shape)
# print(df.columns)

#to find diversity within the columns
unique = df.nunique()
# print(unique)

# to count unique values
survived_unique = df['survived'].unique()
# print(f"The survived column has {survived_unique} values")

sex_unique = df['sex'].unique()
# print(f"The sex are {sex_unique}")

gender_value_count = df['sex'].value_counts()
# print(gender_value_count)

#groupby()
# to seperate the passenger based on gender and then count how many survived

group_data = df.groupby(['sex','survived'])['survived'].count()
# print(group_data)

class_survived = df.groupby(['pclass','survived'])['survived'].count()
# print(class_survived)

embarked_class_survived = df.groupby(["embark_town",'pclass','survived'])["survived"].count()
# print(embarked_class_survived)

#sns count of survival by gender
# sns.countplot(x="sex",hue="survived",data = df)
# plt.xlabel("Gender")
# plt.ylabel("Number of passengers")
# plt.title("Survival by gender")
# plt.show()


#sns catplot=used for creating categorical plots
# sns.catplot(x="embark_town",hue="survived",col='pclass',data=df,kind = "count", palette="Set3")
# plt.xlabel("Embarkation town")
# plt.ylabel("no of passengers")
# plt.title("Survival by Embarkation town and passenger class")
# plt.show()


#describe()
# print(df.describe())


# for describing any one attribute
# print(df["embark_town"].describe())

#dropping columns:survive and alive are same here or no?
# print(df["survived"].value_counts())
# print(df["alive"].value_counts())

df.drop(columns=["alive"],inplace=True)
# print(df.info())

# print(df["embark_town"].value_counts())
# print(df["embarked"].value_counts())
df.drop(columns="embarked",inplace=True)
# print(df.columns)
# print(df.info())

#to check class and p class
# print(df['class'].value_counts())
# print(df['pclass'].value_counts())
df.drop(columns=['pclass'],inplace=True)
# print(df.info())

# data manipulation technique : data cleaning and transforming
# print(df["adult_male"].value_counts())
#we use replacing here
df["adult_male"].replace({True:1,False:0},inplace=True)
# print(df["adult_male"].value_counts())


# missing values and their implications
# print(df.isnull().sum())     #output tells that survived,sex etc have no missing values



# deletion method to remove missing values
# df.dropna(subset=["age"],inplace=True)

#method 2 : imputation method:
#we visualize using a boxplot to see if anything falls as outliers
# sns.boxplot(y="age",data=df)
# plt.title("Box plot for age column")
# plt.show()   # here the output boxplot that we got,the lowest line is Q1,middle line is Q2,last line ie somewhere near 40 is Q3
 
#  lets impute the missing values in the age column with the median
df['age']=df["age"].fillna(df['age'].median())

#Deck column(missing value of 688)
#replace the missing value with most frequent deck value
df['deck']=df["deck"].fillna(df['deck'].mode()[0])
# print(df)
# print(df['deck'])


# lets move to embark_town
# its categorical too but with fewer distinct values

#drop rows with misssing values in the "embark town" column
df.dropna(subset=["embark_town"],inplace=True)
# print(df.isnull().sum())

#lets rename
df.rename(columns = {"deck":"cabin"},inplace=True)
# print(df.columns)


#histogram
# plt.hist(df["who"],color = "skyblue",edgecolor = "black") 
# plt.xlabel("Passenger type")
# plt.ylabel("Frequency")
# plt.title("dist of passenger type")
# plt.show()


#create corr matrix
numeric_df = df.select_dtypes(include=["int64",'float64'])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,cmap="PuBuGn",fmt=".2f")
plt.title("corr matrix of titanic dataset")
plt.show()

# %%
