# 2023 Boston Marathon Analysis

## Objective
For this project I took data form the 2023 Boston Marathon and analyzed it using Python with a goal of analyzing and understanding
performance trends.

## Data
The dataset I used included info from over 26,000 participants with fields for gender, age, finishing time, halfway time

## Methodology 
To be able to use the data, I handled missing values, and convert time variables to minutes. I grouped participants by gender
and age, and use visualizations to identify patterns.

## Key Findings
### Gender Differences
Looking at gender you can see slightly more men ran this race.
This would be interesting to get data from past years going all the way back to 1967 to see the progrression of womem runners 
over the past 60 years
![Gender Counts](gender_distribution.png)

### Age Group Distribution
This graph shows the largest age group is 18-39 years old which is over double the amount of all the other age groups. 
There is a clear trend that the older the age group gets the lower the number of participants. 
![Age Distribution](age_distribution.png)

### Finishing Times
This graph shows the distribution of finishing times of the different age groups. A trend is that the older groups run slower, 
the median slowly goes up. It also should be known the Boston Marathon has qualifying times which I believe keeps the average
completion time down. 
![Finishing Times](finishing_times.png)

### Half Split Difference
This graph was the most interesting to me. This shows the difference in times between the second half of the marathon and the first half. 
It is worth noting how many people had a slower second half compared to the first. There also appears to be trend showing that most people did not
differ much as most of the people were only slower by around 15-20 minutes.
![Half Splits](half_split_differences.png)

