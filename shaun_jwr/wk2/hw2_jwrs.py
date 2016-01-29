'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('police-killings-altered.csv')

killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={
    'lawenforcementagency': 'agency',
    'raceethnicity': 'race'
    }, inplace=True)

# 2. Show the count of missing values in each column

len(killings.index) - killings.count()

# 3. replace each null value in the dataframe with the string "Unknown"

killings.fillna("Unknown")

# 4. How many killings were there so far in 2015?

killings.year.describe()
print len(killings.year)

# 5. Of all killings, how many were male and how many female?

killings.gender.value_counts()

# 6. How many killings were of unarmed people?

unarmedkill = killings.armed.value_counts()['No']
print int(unarmedkill)

# 7. What percentage of all killings were unarmed?

print int((float(unarmedkill)/len(killings.armed)) * 100)

# 8. What are the 5 states with the most killings?

killings.state.value_counts()[0:5]

# 9. Show a value counts of deaths for each race

killings.race.value_counts()

# 10. Display a histogram of ages of all killings

plt.hist(killings.age, color='red', normed=1)
plt.title("Histogram of killings by age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 11. Show 6 histograms of ages by race

killings.age.hist(
    by=killings.race, sharex=False, sharey=False, color='red', normed=1
    )

plt.show()

# 12. What is the average age of death by race?

killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month

pltheight = np.array(killings.month.value_counts())

month = killings.month.unique()
nok = np.arange(len(month))

plt.bar(nok, pltheight)
plt.xticks(nok, month)
plt.xlabel("Month")
plt.ylabel("Number of Killings")

# Less morbid

majors = pd.read_csv('college-majors-altered.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

majors.drop(['Employed_full_time_year_round', 'Major_code'], axis=1)
majors.head()

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

tx = majors.groupby('Major').Median.mean().sort_values(ascending=True).tail(10)

for i in range(len(tx)):
    print tx.index[i]

# 4. Plot the data from the last question in a bar chart, include proper title,
# and labels!

plt.bar(np.arange(len(tx)), tx)
plt.xticks(np.arange(len(tx)), np.array(tx.index), rotation=90)
plt.xlabel("Type of major")
plt.ylabel("Salary")
plt.title("Salary by type of major")
plt.show()

# 5. What is the average median salary for each major category?

ams = majors.groupby("Major_category").Median.mean()

ams

# 6. Show only the top 5 paying major categories

ams.sort_values().tail(5)

# 7. Plot a histogram of the distribution of median salaries

plt.hist(majors.Median, color='red', normed=True)
plt.title("Histogram of distribution of median salaries")
plt.xlabel("Median Salary")
plt.ylabel("Frequency Density")
plt.show()

# 8. Plot a histogram of the distribution of median salaries by major category

plt.hist(majors.groupby('Major_category').Median.mean(), color='red')
plt.title("Histogram of distribution of median salaries by major category")
plt.xlabel("Median Salary")
plt.ylabel("Frequency Density")
plt.show()

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?

majors[['Major', 'Unemployment_rate', 'Unemployed']].sort_values(
    by='Unemployed',
    ascending=True
    ).tail(10)

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for
# each category
# What are the unemployment rates?

unempcat = majors.groupby('Major_category').Unemployment_rate.mean() * 100.0
unempcat.sort_values().tail(10)

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for
# each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = (majors['Employed']/majors['Total'])

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"

majors['sample_unemployment_rate'] = 1-majors['sample_employment_rate']
