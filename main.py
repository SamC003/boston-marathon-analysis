
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("boston_marathon_2023.csv")

print(list(df.columns))
print(df.head())
print(df.describe())
print(df.info())

print()
print(df['gender'].unique())

num_males = (df['gender'] == 'M').sum()
num_females = (df['gender'] == 'W').sum()

print('Number of Females: ', num_females)
print('Number of Males: ', num_males)

gender_counts = df['gender'].value_counts()
gender_counts.plot(kind = 'pie')
plt.title('Gender Distribution (Man/Woman)')
plt.show()

#fix cols to be uniform
#convert times to number
#handle missing values
#standardize genders
#crate useful cols

def hms_to_minutes(x):
    if pd.isna(x):
        return np.nan
    s = str(x).upper().replace(' ', '')
    h = re.search(r'(\d+)H', s)
    m = re.search(r'(\d+)M', s)
    sec = re.search(r'(\d+)S', s)

    hours = int(m.group(1)) if h else 0
    minutes = int(m.group(1)) if m else 0
    seconds = int(sec.group(1)) if sec else 0

    return hours * 60 + minutes + seconds / 60

#What is the spread of the first half - second half
df['half_time_minutes'] = df['half_time'].apply(hms_to_minutes)
df['half_time_minutes'] = df['half_time_minutes'].round()
df['half_time_minutes'] = df['half_time_minutes'].astype('Int64')

df['finish_net_minutes'] = df['finish_net'].apply(hms_to_minutes)
df['finish_net_minutes'] = df['finish_net_minutes'].round()
df['finish_net_minutes'] = df['finish_net_minutes'].astype('Int64')

df['second_half_minutes'] = df['finish_net_minutes'] - df['half_time_minutes']

df['difference_halves_minutes'] = df['second_half_minutes'] - df['half_time_minutes']

# 1) Clean the series
diff = df['difference_halves_minutes'].replace([np.inf, -np.inf], np.nan).dropna()

# 2) Trim outliers (winsorize to 1st–99th percentile)
lo, hi = diff.quantile([0.01, 0.99])
diff_clip = diff.clip(lo, hi)

# 3a) SIMPLE: Histogram with wider bins (15-minute buckets)
bins = np.arange(np.floor(diff_clip.min()/15)*15, np.ceil(diff_clip.max()/15)*15 + 15, 15)

plt.figure(figsize=(10,5))
plt.hist(diff_clip, bins=bins)
plt.title('Difference in Half Splits (2nd − 1st) — 15-minute bins, 1–99% range')
plt.xlabel('Minutes (positive = slower 2nd half)')
plt.ylabel('Number of runners')
plt.tight_layout()
plt.show()

