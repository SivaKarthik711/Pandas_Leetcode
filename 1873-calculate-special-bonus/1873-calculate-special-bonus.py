import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if (row['employee_id'] % 2 != 0 and not row['name'].startswith('M')) else 0,
        axis=1
    )
    employees = employees.sort_values(by='employee_id', ascending=True)
    
    return employees[['employee_id', 'bonus']]
