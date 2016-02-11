'''Nelson Lau GA Data Science Lesson 01 OPTIONAL HW'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to
data_folder = 'C:\\Users\\Nelson\\SG_DAT1\\homework\\data\\'
killings = pd.read_csv('%s\police-killings.csv' % data_folder)
print killings.head()


# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
print "\n---1---"
killings.rename(columns={
                    'lawenforcementagency':'agency',
                    'raceethnicity': 'race'},
                inplace=True)
print killings.head()


# 2. Show the count of missing values in each column
print "\n---2---"
print killings.isnull().sum()


# 3. replace each null value in the dataframe with the string "Unknown"
print "\n---3---"
null_rows = killings.isnull().any(axis = 1)
print "\n>>>ORIGINAL rows with missing values:"
print killings[null_rows]
killings.fillna(value='Unknown',inplace=True)
print "\n>>>UPDATED rows with missing values:"
print killings[null_rows]


# 4. How many killings were there so far in 2015?
print "\n---4---"
print len(killings)


# 5. Of all killings, how many were male and how many female?
print "\n---5---"
print killings.groupby('gender').size()


# 6. How many killings were of unarmed people?
print "\n---6---"
print len(killings[killings['armed'].str.upper() == 'NO'])


# 7. What percentage of all killings were unarmed?
print "\n---7---"
unarmed_percent = float(len(killings[killings['armed'].str.upper() == 'NO'])) / len(killings) *100
print "%0.2f%% of all killings were unarmed" % unarmed_percent 


# 8. What are the 5 states with the most killings?
print "\n---8---"
print killings.groupby('state').size().nlargest(5)


# 9. Show a value counts of deaths for each race
print "\n---9---"
print killings.groupby('race').size()


# 10. Display a histogram of ages of all killings
print "\n---10---"
import matplotlib.pyplot as plt
plt.figure()
killings['age'].plot(kind='hist',title='Ages')
plt.show()


# 11. Show 6 histograms of ages by race
print "\n---11---"
min_age = min(killings['age'])
max_age = max(killings['age'])
fig = plt.figure()
current_plot = 1
for race in killings['race'].unique():
    plt.subplot(3,2,current_plot)
    killings[killings['race'] == race]['age'].plot(kind='hist', title=race, range=[min_age,max_age])
    current_plot += 1
fig.suptitle('Ages', fontsize = 14)
plt.show()


# 12. What is the average age of death by race?
print "\n---12---"
print killings.groupby('race')['age'].mean()


# 13. Show a bar chart with counts of deaths every month
print "\n---13---"

death_by_month = killings.groupby(['month']).size().reset_index() #all the killings are from 2015
months = ['January','February','March','April','May','June'] #these are the only months in the dataset
mapping = {month: i for i, month in enumerate(months)}
key = death_by_month['month'].map(mapping)
death_by_month = death_by_month.iloc[key.argsort()]
death_by_month.rename(columns={0:'killings'}, inplace = True)

death_by_month_plot = death_by_month.plot(kind='bar',x='month',legend = False)
death_by_month_plot.set_xlabel('month')
death_by_month_plot.set_ylabel('deaths')
death_by_month_plot.set_xticklabels(death_by_month_plot.xaxis.get_majorticklabels(), rotation=0)
plt.show()