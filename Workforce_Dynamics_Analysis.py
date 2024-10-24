#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Read in the dataset
pd.set_option("display.max_columns", None)
data = pd.read_csv("C:\\Users\\Administrator\\Downloads\\4_5796499944424609577 (1).csv")
data.sample(10)


# In[4]:


data.shape


# In[5]:


data.info()


# ### Employee Demographics and Job Roles

# What is the age distribution across different job roles and industries?

# In[6]:


# Set the figure size for better readability
plt.figure(figsize=(14, 8))

# Create a boxplot to visualize the age distribution across job roles
sns.boxplot(x='Job_Role', y='Age', data=data, palette='Set2')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add plot title and labels
plt.title('Age Distribution by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Age')

# Show the plot
plt.show()


# In[7]:


# Set the figure size for better readability
plt.figure(figsize=(14, 8))

# Create a boxplot to visualize the age distribution across industries
sns.boxplot(x='Industry', y='Age', data=data, palette='Set3')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add plot title and labels
plt.title('Age Distribution by Industry')
plt.xlabel('Industry')
plt.ylabel('Age')

# Show the plot
plt.show()


# In[8]:


# Group by Job_Role and Industry and calculate average age
age_distribution = data.groupby(['Job_Role', 'Industry'])['Age'].mean().reset_index()

# Display the resulting table
age_distribution


# The data reveals that the average age of employees varies across job roles and industries. For example, **Data Scientists** in the **Consulting** industry have an average age of 40.16 years, while those in **Retail** are slightly older, averaging 41.5 years. Similarly, **Designers** in **Healthcare** have a higher average age of 42.49 years compared to their counterparts in **IT**, where the average age is 40.02 years. 
# 
# Overall, there is a noticeable variation in employee age depending on both the job role and industry, with some industries, such as **Retail** and **Healthcare**, tending to have slightly older workers on average across multiple roles.

# #### NEXT
# Is there a significant gender disparity in certain job roles or industries?

# In[9]:


data['Gender'].unique()


# In[10]:


# Grouping the data by Job Role, Industry, and Gender to get counts
gender_distribution = data.groupby(['Job_Role', 'Industry', 'Gender']).size().unstack(fill_value=0)

# Display the resulting table
gender_distribution


# From the table above, the count of the different gender for each job role and industry combination can be seen.

# In[11]:


#Calculating the Gender Percentage for Each Job Role and Industry
# Calculate the total count for each job role and industry combination
total_count = gender_distribution.sum(axis=1)

# Calculate the percentage of males and females
gender_percentage = gender_distribution.div(total_count, axis=0) * 100

# Display the resulting table with percentages
gender_percentage


# The table above shows the percentage of each gender under a certain job role in a specified industry

# ### Identify Significant Gender Disparity

# In[12]:


# Filter roles where one gender is above 70% in any job role or industry
significant_disparity = gender_percentage[(gender_percentage > 70) | (gender_percentage < 30)]

# Display roles with significant gender disparity
significant_disparity.dropna()


# In[13]:


# Time to visualize the table on gender disparities

# Plot gender distribution for each job role and industry
gender_distribution.plot(kind='bar', stacked=True, figsize=(14, 8))

# Add titles and labels
plt.title('Gender Distribution by Job Role and Industry')
plt.xlabel('Job Role and Industry')
plt.ylabel('Number of Employees')
plt.xticks(rotation=90)
plt.show()


# #### NEXT
# How do years of experience vary across different job roles or industries?

# In[14]:


# Grouping the data by Job Role and Industry and calculating the mean of Years_of_Experience
experience_variation = data.groupby(['Job_Role', 'Industry'])['Years_of_Experience'].mean().reset_index()

# Renaming the last column to Avg_Years_of_Experience
experience_variation.rename(columns={'Years_of_Experience': 'Avg_Years_of_Experience'}, inplace=True)

# Creating a pivot table with Job Role as the index and Industry as the columns
pivot_table = experience_variation.pivot_table(index='Job_Role', columns='Industry', values='Avg_Years_of_Experience')

# Sorting the columns based on the average years of experience (mean of each column)
sorted_columns = pivot_table.mean().sort_values(ascending=False).index
sorted_pivot_table = pivot_table[sorted_columns]

# Display the resulting pivot table
sorted_pivot_table


# In[15]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plotting the variation of years of experience
plt.figure(figsize=(14, 8))
sns.barplot(x='Job_Role', y='Avg_Years_of_Experience', hue='Industry', data=experience_variation)

# Add titles and labels
plt.title('Variation of Years of Experience by Job Role and Industry')
plt.xlabel('Job Role')
plt.ylabel('Average Years of Experience')
plt.xticks(rotation=90)
plt.show()


# ### Work Environment and Hours

# What is the average number of hours worked per week across different job roles?

# In[16]:


# Grouping the data by Job Role and calculating the mean of Hours_Worked_Per_Week
average_hours_worked = data.groupby('Job_Role')['Hours_Worked_Per_Week'].mean().reset_index()

# Renaming the last column to Avg_Hours_Worked_Per_Week
average_hours_worked.rename(columns={'Hours_Worked_Per_Week': 'Avg_Hours_Worked_Per_Week'}, inplace=True)

# Display the resulting table
average_hours_worked


# #### NEXT
# How does the number of virtual meetings correlate with job roles or work locations?

# In[17]:


# Grouping the data by Job Role and calculating the mean of Number_of_Virtual_Meetings
virtual_meetings_by_role = data.groupby('Job_Role')['Number_of_Virtual_Meetings'].mean().reset_index()

# Grouping the data by Work Location and calculating the mean of Number_of_Virtual_Meetings
virtual_meetings_by_location = data.groupby('Work_Location')['Number_of_Virtual_Meetings'].mean().reset_index()

# Renaming the last columns for clarity
virtual_meetings_by_role.rename(columns={'Number_of_Virtual_Meetings': 'Avg_Virtual_Meetings'}, inplace=True)
virtual_meetings_by_location.rename(columns={'Number_of_Virtual_Meetings': 'Avg_Virtual_Meetings'}, inplace=True)

# Display the resulting tables
virtual_meetings_by_location


# In[18]:


virtual_meetings_by_role


# In[19]:


# Visualizing the Data

# Set up the matplotlib figure
plt.figure(figsize=(14, 6))

# Bar plot for average virtual meetings by Job Role
plt.subplot(1, 2, 1)
sns.barplot(data=virtual_meetings_by_role, x='Job_Role', y='Avg_Virtual_Meetings', palette='viridis')
plt.title('Average Virtual Meetings by Job Role')
plt.xticks(rotation=45)
plt.ylabel('Average Number of Virtual Meetings')
plt.xlabel('Job Role')

# Bar plot for average virtual meetings by Work Location
plt.subplot(1, 2, 2)
sns.barplot(data=virtual_meetings_by_location, x='Work_Location', y='Avg_Virtual_Meetings', palette='viridis')
plt.title('Average Virtual Meetings by Work Location')
plt.xticks(rotation=45)
plt.ylabel('Average Number of Virtual Meetings')
plt.xlabel('Work Location')

# Show the plots
plt.tight_layout()
plt.show()


# ### NEXT
# Is there a difference in work-life balance ratings between those working in-office vs. remotely?

# In[20]:


# Grouping the data by Work Location and calculating the mean of Work_Life_Balance_Rating
work_life_balance_comparison = data.groupby('Work_Location')['Work_Life_Balance_Rating'].mean().reset_index()

# Renaming the column for clarity
work_life_balance_comparison.rename(columns={'Work_Life_Balance_Rating': 'Avg_Work_Life_Balance_Rating'}, inplace=True)

# Display the resulting table
work_life_balance_comparison


# From this table, we can see that people who work as hybrid have a more balance work-life rating. However, all three groups have very close average rating.

# In[21]:


# Set up the matplotlib figure
plt.figure(figsize=(8, 5))

# Bar plot for average work-life balance ratings
sns.barplot(data=work_life_balance_comparison, x='Work_Location', y='Avg_Work_Life_Balance_Rating', palette='pastel')
plt.title('Average Work-Life Balance Ratings by Work Location')
plt.ylabel('Average Work-Life Balance Rating')
plt.xlabel('Work Location')

# Show the plot
plt.show()


# ### Stress and Mental Health

# What is the relationship between hours worked per week and stress levels?

# In[22]:


# Mapping stress levels to numeric values
stress_mapping = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

data['Stress_Level_Numeric'] = data['Stress_Level'].map(stress_mapping)

# Check the mapping
print(data[['Stress_Level', 'Stress_Level_Numeric']].head(3))


# In[23]:


# Dropping rows with NaN values in the new Stress Level column
data = data.dropna(subset=['Stress_Level_Numeric'])

# Calculating the correlation between Hours_Worked_Per_Week and the new numeric Stress_Level
correlation = data['Hours_Worked_Per_Week'].corr(data['Stress_Level_Numeric'])

# Display the correlation coefficient
print("Correlation between Hours Worked Per Week and Stress Level:", correlation)


# The interesting thing here is, from this dataset there is almost no linear relationship between the number of hours worked per week and stress levels.

# #### NEXT
# How does stress level vary with job roles, industries, or work locations?

# **1. Stress Level Variation by Job Roles**

# In[24]:


# Grouping by Job Role and counting occurrences of each stress level
stress_by_job_role = data.groupby(['Job_Role', 'Stress_Level']).size().unstack(fill_value=0)

# Display the resulting table
stress_by_job_role


# In[25]:


# Creating the side-by-side bar chart for Stress Level Variation by Job Roles
stress_by_job_role.plot(kind='bar', stacked=False)

# Adding labels and title
plt.xlabel('Job Role')
plt.ylabel('Number of Employees')
plt.title('Stress Levels Distribution by Job Role')
plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
plt.legend(title='Stress Level')
plt.tight_layout()  # Adjust layout for better fit
plt.show()  # Display the plot


# **2. Stress Level Variation by Industries**

# In[26]:


# Grouping by Industry and counting occurrences of each stress level
stress_by_industry = data.groupby(['Industry', 'Stress_Level']).size().unstack(fill_value=0)

# Display the resulting table
stress_by_industry


# The output presents the distribution of stress levels—high, low, and medium—across various industries. 
# - Notably, the Finance sector exhibits the highest number of employees reporting high stress levels (266), indicating a potential issue with workload or job demands in this field. 
# - Conversely, the Manufacturing industry shows the lowest count of high stress levels (215), suggesting a relatively less stressful work environment. 
# 
# In terms of medium stress, the Education industry has the highest count (247), while the IT sector ranks the lowest in this category (240). Overall, these figures reflect varied stress experiences among industries, with Finance and Education facing particular challenges that may warrant further investigation into employee well-being and workplace conditions.

# **3. Stress Level Variation by Work Locations**

# In[27]:


# Grouping by Work Location and counting occurrences of each stress level
stress_by_work_location = data.groupby(['Work_Location', 'Stress_Level']).size().unstack(fill_value=0)

# Display the resulting table
stress_by_work_location


# **DEDUCTION:**
# Remote workers report the highest high stress levels (590), indicating potential stressors associated with this setup. Hybrid employees experience slightly lower high stress (561), while onsite workers have the least (535). Additionally, remote workers also face the highest medium stress levels (577), suggesting challenges in achieving work-life balance. Overall, these findings highlight the mental health implications of remote work, pointing to the need for better support strategies for remote employees.

# #### NEXT 
# Is there a correlation between access to mental health resources and stress levels or mental health conditions?

# In[28]:


data["Mental_Health_Condition"].head()


# In[29]:


data.head(3)


# In[30]:


print(data['Mental_Health_Condition'].unique(), data['Access_to_Mental_Health_Resources'].unique(), data['Stress_Level'].unique())


# In[31]:


import pandas as pd

# Sample DataFrame creation (replace this with your actual data)
data1 = data.copy()

# Convert categorical variables to numeric
data1['Access_to_Mental_Health_Resources'] = data1['Access_to_Mental_Health_Resources'].map({'No': 0, 'Yes': 1})
data1['Stress_Level'] = data1['Stress_Level'].map({'Low': 1, 'Medium': 2, 'High': 3})

# Calculate correlations
correlation_stress = data1['Access_to_Mental_Health_Resources'].corr(data1['Stress_Level'])

# Calculate the distribution of mental health conditions based on access to resources
mental_health_distribution = data1.groupby('Access_to_Mental_Health_Resources')['Mental_Health_Condition'].value_counts(normalize=True).unstack().fillna(0)

# Display the correlation coefficient
print(f"Correlation between Access to Mental Health Resources and Stress Level: {correlation_stress}")
print("\nDistribution of Mental Health Conditions based on Access to Resources:")
mental_health_distribution


# **Deduction:** 
# These results indicate that the prevalence of mental health conditions (Anxiety, Burnout, Depression) is fairly similar regardless of access to mental health resources. Notably, the percentage of employees reporting "None" of these conditions is slightly lower among those with access to resources. Overall, this suggests that while access to mental health resources exists, it does not significantly reduce the incidence of mental health issues in the workforce.

# ### Work-Life Balance and Satisfaction

# How does work-life balance rating correlate with the number of virtual meetings or hours worked?

# In[32]:


data["Work_Life_Balance_Rating"].unique()


# In[33]:


# Calculate the correlation between Work Life Balance Rating and Number of Virtual Meetings
correlation_virtual_meetings = data['Work_Life_Balance_Rating'].corr(data['Number_of_Virtual_Meetings'])

# Calculate the correlation between Work Life Balance Rating and Hours Worked Per Week
correlation_hours_worked = data['Work_Life_Balance_Rating'].corr(data['Hours_Worked_Per_Week'])

# Display the correlation coefficients
print(f"Correlation between Work Life Balance Rating and Number of Virtual Meetings: {correlation_virtual_meetings}")
print(f"Correlation between Work Life Balance Rating and Hours Worked Per Week: {correlation_hours_worked}")


# **Deduction:** Overall, both correlation coefficients suggest that neither the number of virtual meetings nor the hours worked per week have a meaningful impact on employees' assessments of their work-life balance. This could imply that factors other than virtual meeting frequency and work hours might play a more critical role in influencing work-life balance, such as organizational culture, job demands, or individual coping strategies.

# In[34]:


data.head(3)


# In[35]:


# Mapping categorical values to numerical values
productivity_map = {'Decrease': -1, 'No Change': 0, 'Increase': 1}
data['Productivity_Change_Numeric'] = data['Productivity_Change'].map(productivity_map)

# Grouping by Job Role and Work Location and calculating the average productivity change
average_productivity = data.groupby(['Job_Role', 'Work_Location'])['Productivity_Change_Numeric'].mean().reset_index()

# Renaming the column for clarity
average_productivity.rename(columns={'Productivity_Change_Numeric': 'Avg_Productivity_Change'}, inplace=True)

# Displaying the resulting table
average_productivity


# In[36]:


data.head(3)


# In[ ]:




