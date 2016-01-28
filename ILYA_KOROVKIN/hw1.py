'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)
killings.head(1)
killings.columns

# 2. Show the count of missing values in each column

killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"

killings.fillna(value = 'Unknown', inplace = True)

# 4. How many killings were there so far in 2015?

killings.name[killings['year'] == 2015].count()
# 467

# 5. Of all killings, how many were male and how many female?

killings.name[killings['gender'] == 'Male'].count()
killings.name[killings['gender'] == 'Female'].count()
# Male - 445, Female - 22


# 6. How many killings were of unarmed people?

killings.name[killings['armed'] == 'No'].count()
# 102

# 7. What percentage of all killings were unarmed?

round(100*killings.name[killings['armed'] == 'No'].count()/float(killings.name.count()),2)
# 21.84%

# 8. What are the 5 states with the most killings?

killings.state.value_counts().head(5)

'''
CA    74
TX    46
FL    29
AZ    25
OK    22
'''

# 9. Show a value counts of deaths for each race

killings.race.value_counts()

'''
White                     236
Black                     135
Hispanic/Latino            67
Unknown                    15
Asian/Pacific Islander     10
Native American             4
'''

# 10. Display a histogram of ages of all killings

killings.age.hist(bins=14)

# 25-35 years is the 10-year range with the highest number of killings

# 11. Show 6 histograms of ages by race

killings.age.hist(by=killings.race, sharex=True, sharey=True, bins=14)

# 12. What is the average age of death by race?

killings.groupby('race').age.apply(lambda x: round(x.mean(),0))

'''
race
Asian/Pacific Islander    41
Black                     34
Hispanic/Latino           32
Native American           28
Unknown                   44
White                     40
'''


# 13. Show a bar chart with counts of deaths every month

killings.month.value_counts().ix[['January', 'February', 'March', 'April', 'May', 'June']].plot(kind='bar')
#using ix[neworderlist] to have months looking chronologically ordered

###################
### Less Morbid ###
###################

majors = pd.read_csv('hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

del majors['Employed_full_time_year_round']
del majors['Major_code']

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

majors[['Major', 'Median']].sort_index(by='Median', ascending = False).head(10)

'''
	Major	Median
59	PETROLEUM ENGINEERING	125000
154	PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTR...	106000
57	NAVAL ARCHITECTURE AND MARINE ENGINEERING	97000
55	METALLURGICAL ENGINEERING	96000
58	NUCLEAR ENGINEERING	95000
56	MINING AND MINERAL ENGINEERING	92000
97	MATHEMATICS AND COMPUTER SCIENCE	92000
48	ELECTRICAL ENGINEERING	88000
45	CHEMICAL ENGINEERING	86000
51	GEOLOGICAL AND GEOPHYSICAL ENGINEERING	85000
'''

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!

majors[['Major', 'Median']].sort_values(by='Median', ascending = False).head(10).plot(kind='bar', title = '10 Best Paying Majors')
plt.xlabel('Majors')
plt.ylabel('Annual Salary in USD')

# 5. What is the average median salary for each major category?

majors.groupby('Major_category', as_index=False).Median.mean().sort_values(by='Median', ascending = False)

'''
	Major_category	Median
7	Engineering	77758.620690
5	Computers & Mathematics	66272.727273
13	Physical Sciences	62400.000000
3	Business	60615.384615
8	Health	56458.333333
0	Agriculture & Natural Resources	55000.000000
15	Social Science	53222.222222
12	Law & Public Policy	52800.000000
10	Industrial Arts & Consumer Services	52642.857143
2	Biology & Life Science	50821.428571
4	Communications & Journalism	49500.000000
9	Humanities & Liberal Arts	46080.000000
14	Psychology & Social Work	44555.555556
6	Education	43831.250000
1	Arts	43525.000000
11	Interdisciplinary	43000.00000
'''

# 6. Show only the top 5 paying major categories

majors.groupby('Major_category', as_index=False).Median.mean().sort_values(by='Median', ascending = False).head(5)

# 7. Plot a histogram of the distribution of median salaries

majors.Median.hist(bins=18)

# 8. Plot a histogram of the distribution of median salaries by major category

majors.Median.hist(by=majors.Major_category, sharex=True, sharey=True, bins=14)

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?

majors[['Major', 'Unemployed', 'Unemployment_rate']].sort_values(by='Unemployed', ascending = False).head(10)
'''
	Major	Unemployed	Unemployment_rate
161	BUSINESS MANAGEMENT AND ADMINISTRATION	147261	0.058865
158	GENERAL BUSINESS	85626	0.051378
114	PSYCHOLOGY	79066	0.069667
159	ACCOUNTING	75379	0.053415
13	COMMUNICATIONS	54390	0.064360
73	ENGLISH LANGUAGE AND LITERATURE	52248	0.068645
164	MARKETING AND MARKETING RESEARCH	51839	0.055033
132	POLITICAL SCIENCE AND GOVERNMENT	40376	0.069374
25	GENERAL EDUCATION	38742	0.043904
78	BIOLOGY	36757	0.059301
'''

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category

majors.groupby('Major_category', as_index=False).Unemployed.mean().sort_values(by='Unemployed', ascending = False).head(10)
'''
	Major_category	Unemployed
3	Business	33415.153846
4	Communications & Journalism	25299.750000
15	Social Science	14683.333333
1	Arts	13015.625000
9	Humanities & Liberal Arts	11942.400000
14	Psychology & Social Work	11578.444444
12	Law & Public Policy	8609.800000
6	Education	7833.500000
5	Computers & Mathematics	7270.363636
8	Health	6251.083333
'''

# What are the unemployment rates?

majors.groupby('Major_category', as_index=False).Unemployment_rate.mean().sort_values(by='Unemployment_rate', ascending = False).head(10)
'''
Major_category	Unemployment_rate
1	Arts	0.087601
14	Psychology & Social Work	0.077867
11	Interdisciplinary	0.077269
9	Humanities & Liberal Arts	0.069429
4	Communications & Journalism	0.069125
12	Law & Public Policy	0.067854
15	Social Science	0.065686
5	Computers & Mathematics	0.059437
10	Industrial Arts & Consumer Services	0.058546
13	Physical Sciences	0.054541
'''

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = majors.Employed / majors.Total

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"

majors['sample_unemployment_rate'] = 1 - majors.sample_employment_rate

majors.groupby('Major_category', as_index=False).sample_unemployment_rate.mean().sort_values(by='sample_unemployment_rate', ascending = False)
'''
Sample uneployment rates are much higher than declared unemployment rates

	Major_category	sample_unemployment_rate
6	Education	0.365460
9	Humanities & Liberal Arts	0.320975
14	Psychology & Social Work	0.311081
13	Physical Sciences	0.282752
15	Social Science	0.281793
10	Industrial Arts & Consumer Services	0.281672
2	Biology & Life Science	0.280232
8	Health	0.279420
7	Engineering	0.272249
1	Arts	0.258402
12	Law & Public Policy	0.245698
0	Agriculture & Natural Resources	0.244195
3	Business	0.213851
4	Communications & Journalism	0.212782
11	Interdisciplinary	0.210027
5	Computers & Mathematics	0.198305
'''
