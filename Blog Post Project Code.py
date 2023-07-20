#!/usr/bin/env python
# coding: utf-8

# # Writing a Data Scientist Blog Post Project

# # Data Wrangling

# In[182]:


#importing libraries needed 
#importing numpy package
import numpy as np
#importing pandas package
import pandas as pd
#importing matplotlib package
import matplotlib.pyplot as plot  
get_ipython().run_line_magic('matplotlib', 'inline')

#read in data 
df = pd.read_csv('survey_results_public.csv')
schema = pd.read_csv('survey_results_schema.csv')
#view first 5 rows
df.head()


# In[19]:


#visualizing the questions of the survey
schema_string = schema.to_string()
print(schema_string)


# In[170]:


#finding the number of nan values in the columns needed for our questions
selected_columns = [31,29,12,19,18,152,83]
missing_values_count = df.iloc[:, selected_columns].isna().sum()
print(missing_values_count)


# # Dealing with missing values

# In[128]:


#viewing first five salary values for respondents
salary = df['Salary'].value_counts()
salary.head()
#filling in nan salary values with mean
mean_sal = df['Salary'].mean()
df['Salary'].fillna(mean_sal, inplace=True)
salary.head()


# In[127]:


#viewing first five job satisfaction values for respondents
Job_S = df['JobSatisfaction'].value_counts()
Job_S.head()
#filling in nan job satisfaction values with mean
mean_job = df['JobSatisfaction'].mean()
df['JobSatisfaction'].fillna(mean_job, inplace=True)
Job_S.head()


# In[130]:


#viewing first five years coded in job values for respondents
years_coded = df['YearsCodedJob'].value_counts().reset_index()
years_coded.head()
#filling in nan 'YearsCodedJob' values through back anf foward filling
years_coded.fillna(method='ffill')
years_coded.fillna(method='bfill')


# In[131]:


#viewing the first five values from the 'ProblemSolving' column
answers_size = df['ProblemSolving'].value_counts().reset_index()
answers_size.head()
#filling in nan 'ProblemSolving' values through back and foward filling
answers_size.fillna(method='ffill')
answers_size.fillna(method='bfill')


# In[171]:


#viewing the first five values from the 'LearningNewTech' column
answers_remote = df['LearningNewTech'].value_counts().reset_index()
answers_remote.head()
#filling in nan 'LearningNewTech' values through back and foward filling
answers_remote.fillna(method='ffill')
answers_remote.fillna(method='bfill')


# In[159]:


#viewing the first five answers to the 'EducationTypes' column
gif_a = df['EducationTypes'].value_counts().reset_index()
gif_a.head()
#filling in the nan 'EducationTypes' values through back and foward filling
gif_a.fillna(method='ffill')
gif_a.fillna(method='bfill')


# In[172]:


#viewing the first five answers to the 'CareerSatisfaction' columns
ser = df['CareerSatisfaction'].value_counts().reset_index()
ser.head()
#filling in the nan 'CareerSatisfaction' values with the columns mean
mean_career = df['CareerSatisfaction'].mean()
df['CareerSatisfaction'].fillna(mean_career, inplace=True)
ser.head()


# # Question 1

# ### Do Developers Who Have Coded For Longer as a Part of Their Job Have a Higher or Lower Salary and Job Satisfaction?

# In[121]:


#viewing the table of coorelation of salary and years of coding in job
hap = df.groupby('YearsCodedJob')['Salary'].mean().sort_values()
hap


# In[195]:


#making graph displaying the coorelation of salary and years of coding in job
plot.bar(hap.index, hap)
plot.xlabel('Years Coded in Job')
plot.ylabel('Average Salary(USD)')
plot.title("Salary by Amount of Years Coded in Job")
plot.xticks(rotation=55)
plot.show


# In[125]:


#viewing table for the coorelation of job satisfaction and years of coding in job
sal = df.groupby('YearsCodedJob')['JobSatisfaction'].mean().sort_values()
sal


# In[196]:


#making graph showing coorelation of job satisfaction and years of coding in job
plot.bar(sal.index, sal)
plot.xlabel('Years Coded in Job')
plot.ylabel('Average Job Satisfaction')
plot.title("Job Satisfaction by Amount of Years Coded in Job")
plot.xticks(rotation=55)
plot.show


# #  Question 2

# ### Do Devlopers Who Enjoy Learning New Technologies Have Higher Salaries and Job Satisfaction?

# In[210]:


#viewing table displaying values related to the coorelation of the the level of aggreement to the statement, "I enjoy learning new technologies" and the respondent's salary
newt = df.groupby('LearningNewTech')[('Salary')].mean().sort_values()
newt
#creating graph displaying the coorelation of the the level of aggreement to the statement, "I enjoy learning new technologies" and the respondent's salary
plot.bar(newt.index, newt)
plot.xlabel("Level of Agreement to the Statement: I Enjoy Learning New Technologies")
plot.ylabel("Average Salary(USD)")
plot.title("Do Developers Who Enjoy Learning New Technologies Have Higher Salaries?")
plot.xticks(rotation=45)


# In[211]:


#viewing table displaying values related to the coorelation of the the level of aggreement to the statement, "I enjoy learning new technologies" and the respondent's job satisfaction
newt_JS = df.groupby('LearningNewTech')[('JobSatisfaction')].mean().sort_values()
newt_JS
#creating graph displaying the coorelation of the the level of aggreement to the statement, "I enjoy learning new technologies" and the respondent's job satisfaction
plot.bar(newt_JS.index, newt_JS)
plot.xlabel("Level of Agreement to the Statement: I Enjoy Learning New Technologies")
plot.ylabel("Average Job Satisfaction")
plot.title("Do Developers Who Enjoy Learning New Technologies Have Higher Job Satisfaction?")
plot.xticks(rotation=45)


# # Question 3

# ### Do Developers Who Enjoy Problem Solving Have Higher Salaries and Job Satisfactions?

# In[209]:


#viewing values for the coorelation of the responses to "I enjoy problem solving" and respondent's salary
solv = df.groupby('ProblemSolving')[('Salary')].mean().sort_values()
solv
#creating graph displaying the coorelation of the responses to "I enjoy problem solving" and respondent's salary
plot.bar(solv.index,solv)
plot.xlabel("Level of Agreement to the Statement: I Enjoy Problem Solving")
plot.ylabel("Average Salary(USD)")
plot.title("Do Developers Who Enjoy Problem Solving Make More Money?")
plot.xticks(rotation=45)
plot.show


# In[203]:


#viewing table displaying the coorelation of the response to the question "I enjoy problem solving" and respondent's job satisfaction
solv_JS = df.groupby('ProblemSolving')[('JobSatisfaction')].mean().sort_values()
solv_JS
#creating a graph displaying the coorelation of the response to the question "I enjoy problem solving" and respondent's job satisfaction
plot.bar( solv_JS.index, solv_JS)
plot.xlabel("Level of Agreement to the Statement: I Enjoy Problem Solving")
plot.ylabel("Job Satisfaction")
plot.title("Do Developers Who Enjoy Problem Solving Have Higher Job Satisfaction?")
plot.xticks(rotation=45)
plot.yticks(size=10)

