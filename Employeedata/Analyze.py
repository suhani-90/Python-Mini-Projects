import pandas as pd
import numpy as np


df=pd.read_csv('cleaned_employee_data.csv')
mean=df['Hours_Worked'].mean()        # Average hours worked
max=df['Tasks_Completed'].max()      # Most tasks by one employee
min=df['Efficiency_Score'].min()     # Lowest efficiency score

eff=df.groupby('Department')['Efficiency_Score'].mean()

agg=df.groupby('Department').agg({
    'Tasks_Completed': 'sum',
    'Hours_Worked': 'mean'
})


print(mean)
print(min)
print(max)

print(eff)
print(agg)

df.describe()