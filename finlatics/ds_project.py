#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"online_advertising_performance_data.csv")
print(df)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.max_columns",None)

print(df.columns)

'''What is the overall trend in user engagement 
throughout the campaign period?'''

user_engagement = df['user_engagement'].value_counts()
print(user_engagement)


'''How does the size of the ad (banner)
impact the number of clicks generated?'''

x = df['banner']
y = df['clicks']
plt.bar(x,y)
plt.xlabel("Banner")
plt.ylabel("Clicks")
plt.title("Impact of the size of the Banner on clicks")
plt.show()


'''Which publisher spaces (placements) yielded the
highest number of displays and clicks?'''

high = df.groupby(["placement"])[["clicks"]].aggregate([min,max,sum,'mean'])
high_disp = df.groupby(["placement"])[['displays']].aggregate([min,max,sum,'mean'])
print(high)
print(high_disp)

# highest displays = mno
# highest clicks = ghi

'''Is there a correlation between the cost of
serving ads and the revenue generated from clicks?'''

numeric_df = df.select_dtypes(include=["int64",'float64'])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_matrix,annot=True,cmap="PuBuGn",fmt=".2f")
plt.title("corr matrix of dataset")
plt.show()
print(corr_matrix["clicks"]["cost"])


'''What is the average revenue generated per click 
for Company X during the campaign period?'''


avg = df["revenue"].mean()
print(avg)


'''Which campaigns had the highest post-click 
conversion rates?'''

high_pc = df.groupby(['campaign_number'])[['post_click_conversions']].aggregate([max])
print(high_pc)


'''Are there any specific trends or patterns in 
post-click sales amounts over time?'''


plt.plot(df['post_click_sales_amount'])
plt.xlabel("time")
plt.ylabel("post_click_sales_amount")
plt.show()


# there seems to be a periodic pattern in post-click sales amounts over time

'''How does the level of user engagement vary 
across different banner sizes?'''

diff_banner = df.groupby(['banner','user_engagement'])['banner'].count()
print(diff_banner)

'''Which placement types result in the highest 
post-click conversion rates?'''

pt = df.groupby(['placement'])[['post_click_conversions']].aggregate([sum])
print(pt)

# highest = ghi


'''Can we identify any seasonal patterns or fluctuations in displays and
clicks throughout the campaign period?'''

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Group data by 'day' and calculate the sum of displays and clicks
daily_data = df.groupby('day').agg({
    'displays': 'sum',
    'clicks': 'sum'
}).reset_index()

# Plotting the daily sum of displays and clicks
plt.figure(figsize=(14, 7))

# Plot displays
plt.subplot(1, 2, 1)
plt.plot(daily_data['day'], daily_data['displays'], marker='o')
plt.title('Daily Sum of Displays')
plt.xlabel('Day of April')
plt.ylabel('Sum of Displays')
plt.grid(True)

# Plot clicks
plt.subplot(1, 2, 2)
plt.plot(daily_data['day'], daily_data['clicks'], marker='o', color='orange')
plt.title('Daily Sum of Clicks')
plt.xlabel('Day of April')
plt.ylabel('Sum of Clicks')
plt.grid(True)

plt.tight_layout()
plt.show()

'''Is there a correlation between user engagement levels and the revenue generated?'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
df = pd.read_csv('online_advertising_performance_data.csv')

# Convert user engagement into an ordered categorical type for correlation analysis
engagement_order = ['Low', 'Medium', 'High']
df['user_engagement'] = pd.Categorical(df['user_engagement'], categories=engagement_order, ordered=True)

# Convert user engagement to codes
df['engagement_code'] = df['user_engagement'].cat.codes

# Calculate the correlation coefficient
correlation = df['engagement_code'].corr(df['revenue'])
print(f"Correlation coefficient: {correlation}")

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='engagement_code', y='revenue', hue='user_engagement', palette='deep', s=100)
plt.xlabel('User Engagement Level (Low=0, Medium=1, High=2)')
plt.ylabel('Revenue')
plt.title('Scatter plot of User Engagement vs Revenue')
plt.grid(True)
plt.show()


'''Are there any outliers in terms of cost, clicks, or revenue that warrant further investigation?'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Function to detect outliers using IQR
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Detect outliers in cost, clicks, and revenue
outliers_cost = detect_outliers(df, 'cost')
outliers_clicks = detect_outliers(df, 'clicks')
outliers_revenue = detect_outliers(df, 'revenue')

# Display outliers
print("Outliers in Cost:")
print(outliers_cost[['cost']])
print("\nOutliers in Clicks:")
print(outliers_clicks[['clicks']])
print("\nOutliers in Revenue:")
print(outliers_revenue[['revenue']])

# Visualize outliers using box plots
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x=df['cost'])
plt.title('Box plot of Cost')

plt.subplot(1, 3, 2)
sns.boxplot(x=df['clicks'])
plt.title('Box plot of Clicks')

plt.subplot(1, 3, 3)
sns.boxplot(x=df['revenue'])
plt.title('Box plot of Revenue')

plt.show()


'''How does the effectiveness of campaigns vary based on the size of the ad and placement type?'''

import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Group data by 'banner' (ad size) and 'placement' and calculate mean values
grouped_data = df.groupby(['banner', 'placement']).agg({
    'clicks': 'mean',
    'revenue': 'mean',
    'post_click_conversions': 'mean'
}).reset_index()

# Sort the data for better readability
sorted_data = grouped_data.sort_values(by=['banner', 'revenue', 'clicks'], ascending=False)

# Display the sorted data
print(sorted_data)


'''Are there any specific campaigns or banner sizes that consistently outperform others in terms of ROI?'''
import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Calculate ROI for each entry
df['ROI'] = (df['revenue'] - df['cost']) / df['cost']

# Group data by 'campaign_number' and 'banner' and calculate mean ROI
grouped_data = df.groupby(['campaign_number', 'banner']).agg({
    'ROI': 'mean'
}).reset_index()

# Sort the data by ROI in descending order to see the top performers
sorted_data = grouped_data.sort_values(by='ROI', ascending=False)

# Display the top performing campaigns and banner sizes
print(sorted_data.head())



'''What is the distribution of post-click conversions across different placement types?'''
import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Group data by 'placement' and calculate sum and mean of post-click conversions
grouped_data = df.groupby('placement').agg({
    'post_click_conversions': ['sum', 'mean']
}).reset_index()

# Rename columns for clarity
grouped_data.columns = ['Placement', 'Total Post-Click Conversions', 'Average Post-Click Conversions']

# Display the results
print(grouped_data)


'''Are there any noticeable differences in user engagement levels between weekdays and weekends?'''
'''The provided dataset does not include specific information 
about the days of the week (e.g., Monday, Tuesday, etc.) but only
includes the day of the month. Therefore, it is not possible to 
directly analyze or determine differences in user engagement 
levels between weekdays and weekends based on the data provided.
To perform such an analysis, additional data indicating the day 
of the week for each entry would be necessary.'''


'''How does the cost per click (CPC) vary across different 
campaigns and banner sizes?'''
import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Calculate Cost Per Click (CPC)
df['CPC'] = df['cost'] / df['clicks']

# Replace infinite values with NaN since division by zero occurs if clicks are zero
df['CPC'].replace([float('inf'), -float('inf')], pd.NA, inplace=True)

# Group data by 'campaign_number' and 'banner' and calculate mean CPC
grouped_data = df.groupby(['campaign_number', 'banner']).agg({
    'CPC': 'mean'
}).reset_index()

# Sort the data by CPC for better readability
sorted_data = grouped_data.sort_values(by='CPC', ascending=True)

# Display the results
print(sorted_data)



'''•	Are there any campaigns or placements that are 
particularly cost-effective in terms of generating post-click 
conversions?'''
import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Calculate Cost Per Conversion (CPCV)
df['CPCV'] = df['cost'] / df['post_click_conversions']

# Replace infinite values with NaN since division by zero occurs if there are no conversions
df['CPCV'].replace([float('inf'), -float('inf')], pd.NA, inplace=True)

# Group data by 'campaign_number' and 'placement' and calculate mean CPCV
grouped_data = df.groupby(['campaign_number', 'placement']).agg({
    'CPCV': 'mean'
}).reset_index()

# Sort the data by CPCV in ascending order to see the most cost-effective combinations
sorted_data = grouped_data.sort_values(by='CPCV', ascending=True)

# Display the most cost-effective campaign and placement combinations
print(sorted_data.head())


'''Can we identify any trends or patterns in post-click conversion rates based on the day of the week?'''

'''Based on the provided dataset, it is not possible to identify
trends or patterns in post-click conversion rates based on the 
day of the week. The dataset includes information about the day 
of the month and various advertising metrics, but it does not 
specify the day of the week (e.g., Monday, Tuesday, etc.). To 
perform an analysis of post-click conversion rates by day of the 
week, additional data indicating the specific day of the week 
for each entry would be necessary. Without this information, 
we cannot determine how post-click conversion rates vary from 
weekdays to weekends or among different weekdays.'''

'''How does the effectiveness of campaigns vary throughout different user engagement types in terms of post-click conversions?'''

import pandas as pd

# Load the data
df = pd.read_csv('online_advertising_performance_data.csv')

# Group data by 'user_engagement' and calculate mean post-click conversions
grouped_data = df.groupby('user_engagement').agg({
    'post_click_conversions': 'mean'
}).reset_index()

# Sort the data by mean post-click conversions for better readability
sorted_data = grouped_data.sort_values(by='post_click_conversions', ascending=False)

# Display the results
print(sorted_data)

