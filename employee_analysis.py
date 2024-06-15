import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("The file does not exist")
        return None

def clean_data(df):
    if df is not None:
        # Renaming columns
        df.columns = ['EmployeeID', 'FirstName', 'LastName', 'Department', 'StartDate', 'Salary', 'EmploymentStatus']
        
        # convert datatype
        df['StartDate'] = pd.to_datetime(df['StartDate'], errors='coerce')
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        
        # Calculation of years of work experience
        current_date = datetime.now()
        df['ExperienceYears'] = (current_date - df['StartDate']).dt.days / 365.25
        
        # Clear any lines with NaN values
        df = df.dropna()
        
        return df
    else:
        print("The DataFrame is empty or not loaded properly")
        return None

def calculate_average_salary(df, department):
    department_df = df[df['Department'].str.strip() == department]
    if not department_df.empty:
        average_salary = department_df['Salary'].mean()
        return average_salary
    else:
        print(f"No data found for department: {department}")
        return None

def find_employees_with_experience(df, years):
    current_date = datetime.now()
    df.loc[:, 'ExperienceYears'] = (current_date - df['StartDate']).dt.days / 365.25
    experienced_employees = df[df['ExperienceYears'] >= years]['FirstName'].str.strip() + ' ' + df['LastName'].str.strip()
    return experienced_employees.dropna().tolist()

def get_department_statistics(df):
    current_date = datetime.now()
    df.loc[:, 'Age'] = (current_date - df['StartDate']).dt.days / 365.25  # Using 365.25 for more accurate year calculation
    
    department_stats = {}
    for department in df['Department'].unique():
        department_df = df[df['Department'] == department]
        average_salary = department_df['Salary'].mean()
        average_age = department_df['Age'].mean()
        department_stats[department] = {'Average Salary': average_salary, 'Average Age': average_age}
    
    return department_stats

def plot_salary_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Salary'], bins=20, color='blue', edgecolor='black')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.savefig('salary_distribution.png')
    plt.close()

def plot_average_salary_by_department(df):
    department_avg_salary = df.groupby('Department')['Salary'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    department_avg_salary.plot(kind='bar', color='green', edgecolor='black')
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.savefig('average_salary_by_department.png')
    plt.close()

def plot_salary_vs_experience(df):
    print("Starting to plot Salary vs. Experience...")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='ExperienceYears', y='Salary', hue='Department')
    plt.title('Salary vs. Experience')
    plt.xlabel('Experience Years')
    plt.ylabel('Salary')
    plt.savefig('salary_vs_experience.png')
    plt.close()
    print("Salary vs. Experience plot saved as salary_vs_experience.png")

def plot_age_distribution_by_department(df):
    print("Starting to plot Age Distribution by Department...")
    current_date = datetime.now()
    df.loc[:, 'Age'] = (current_date - df['StartDate']).dt.days / 365.25  # Ensure that the column names are correct and use 365.25 to calculate the age
    print(df[['Department', 'Age']].head())  # Add debugging information
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Department', y='Age', data=df)
    plt.title('Age Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Age')
    plt.savefig('age_distribution_by_department.png')
    plt.close()
    print("Age distribution by department plot saved as age_distribution_by_department.png")