import employee_analysis as ea

df = ea.load_data('employees.csv')
cleaned_df = ea.clean_data(df)

if cleaned_df is not None:
    print(cleaned_df)
    print(f"Shape of the DataFrame: {cleaned_df.shape}")
else:
    print("No data to display")

print("Checking cleaned DataFrame...")
print(cleaned_df.head())
print(cleaned_df.info())

# Calculation of average wages in designated sectors
average_salary_it = ea.calculate_average_salary(cleaned_df, 'IT')
print(f"Average salary in IT department: {average_salary_it}")

# Find employees with specified years of experience
experienced_employees = ea.find_employees_with_experience(cleaned_df, 5)
print(f"Employees with at least 5 years of experience: {experienced_employees}")

# Access to statistical information by sector
department_stats = ea.get_department_statistics(cleaned_df)
print(f"Department statistics: {department_stats}")

# Check that the data frame exists and that the data is correct
if cleaned_df is not None and not cleaned_df.empty:
    # Mapping of wage distribution
    ea.plot_salary_distribution(cleaned_df)
    print("Salary distribution plot saved as salary_distribution.png")

    # Mapping of average wages by sector
    ea.plot_average_salary_by_department(cleaned_df)
    print("Average salary by department plot saved as average_salary_by_department.png")

# Scatterplotting wages vs. experience
ea.plot_salary_vs_experience(cleaned_df)
print("Salary vs. Experience plot saved as salary_vs_experience.png")

#  Box and line plotting of age distribution by sector
ea.plot_age_distribution_by_department(cleaned_df)
print("Age distribution by department plot saved as age_distribution_by_department.png")
