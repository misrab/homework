import pandas as pd

###################
### Less Morbid ###
###################
data_folder = 'C:\\Users\\Nelson\\SG_DAT1\\homework\\data\\'

majors = pd.read_csv('%s\college-majors.csv' % data_folder)
print majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
print "\n---1---"
majors.drop('Employed_full_time_year_round', axis = 1, inplace=True)
majors.drop('Major_code', axis = 1, inplace=True)
print majors.head()

# 2. Show the count of missing values in each column
print "\n---2---"
print majors.isnull().sum()

# 3. What are the top 10 highest paying majors?
print "\n---3---"
print majors.groupby('Major')['Median'].mean().nlargest(10)


# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
print "\n---4---"
import matplotlib.pyplot as plt
top10_salary_plot = majors.groupby('Major')['Median'].mean().nlargest(10).plot(kind='barh', legend = False)
plt.gca().invert_yaxis()
plt.subplots_adjust(left=0.25)
plt.show()


# 5. What is the average median salary for each major category?
print "\n---5---"
print majors.groupby('Major_category')['Median'].mean()


# 6. Show only the top 5 paying major categories
print "\n---6---"
print majors.groupby('Major_category')['Median'].mean().nlargest(5)


# 7. Plot a histogram of the distribution of median salaries
print "\n---7---"
median_histogram = majors['Median'].plot(kind='hist')
median_histogram.set_xlabel('Median salary')
plt.show()


# 8. Plot a histogram of the distribution of median salaries by major category
print "\n---8---"
median_by_category_histogram = majors.groupby('Major_category')['Median'].mean().plot(kind='hist')
median_by_category_histogram.set_xlabel('Median salary by Major category')
plt.show()


# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
print "\n---9---"
print majors[['Major','Unemployment_rate']].sort_values(by='Unemployment_rate',ascending=False).head(10).to_string(index=False)


# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
print "\n---10---"
print majors.groupby('Major_category')['Unemployment_rate'].mean().nlargest(10)


# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors['sample_employment_rate'] = majors['Employed'] / majors['Total']
print majors.head()


# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_unemployment_rate'] = 1 - majors['sample_employment_rate']
print majors.head()
