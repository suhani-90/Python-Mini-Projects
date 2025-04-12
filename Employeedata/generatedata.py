import pandas as pd
import numpy as np

def create_messy_employee_data(filename='employee_data.csv', num_rows=40):
    np.random.seed(42)

    employee_ids = [100 + i for i in range(num_rows)]
    hours = np.random.choice([8, 7.5, 9, np.nan, -2, 0, np.inf], size=num_rows)
    tasks = np.random.choice([5, 6, 7, 8, 'five', 0, np.nan], size=num_rows)
    efficiency = np.random.choice([0.7, 0.8, 0.9, -0.4, 0, np.nan, np.inf], size=num_rows)
    departments = np.random.choice(['Sales', 'HR', 'Tech', 'Support'], size=num_rows)

    # Add some intentional duplicates
    if num_rows > 20:
        employee_ids[10] = employee_ids[0]
        employee_ids[20] = employee_ids[5]

    # Create DataFrame
    df = pd.DataFrame({
        'Employee_ID': employee_ids,
        'Hours_Worked': hours,
        'Tasks_Completed': tasks,
        'Efficiency_Score': efficiency,
        'Department': departments
    })

    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"✅ Dataset saved as '{filename}' with {num_rows} rows.")

# Run the function
create_messy_employee_data()
