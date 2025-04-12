import pandas as pd
import numpy as np

df=pd.read_csv('employee_data.csv')
print(df.head(5))

#Convert the non numbeeeric value to numeric
df['Tasks_Completed'] = pd.to_numeric(df['Tasks_Completed'], errors='coerce')

#replace all inf and negative inf with nan
df = df.replace([np.inf, -np.inf], np.nan)

#Fill nan values with median ,0 and mean respectively
df['Hours_Worked'] = df['Hours_Worked'].fillna(df['Hours_Worked'].median())
df['Tasks_Completed'] = df['Tasks_Completed'].fillna(0)
df['Efficiency_Score'] = df['Efficiency_Score'].fillna(df['Efficiency_Score'].mean())

#Where value less than 0 fill nan
df.loc[df['Hours_Worked'] <= 0, 'Hours_Worked'] = np.nan
df.loc[df['Efficiency_Score'] < 0, 'Efficiency_Score'] = np.nan

#float to int
df['Hours_Worked'] = df['Hours_Worked'].astype(int)

#add new coloumn
df['Tasks_Per_Hour'] = df['Tasks_Completed'] / df['Hours_Worked']

print(df.head(10))

#add cleaned data to new csv file
df.to_csv('cleaned_employee_data.csv', index=False)

