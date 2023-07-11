emp_id = input("Enter Employee Id: ")
emp_first_name = input("Enter Employee First Name: ")
emp_last_name = input("Enter Employee Last Name: ")
emp_dob = input("Enter Employee DOB(date of birth in YYYY-MM-DD): ")
emp_gender = input("Enter Employee Gender: ")
emp_email = input("Enter Employee Email Address: ")
emp_country = input("Enter Employee Country: ")
emp_salary = input("Enter Employee Salary: ")

employee_dict = {
"emp_id": emp_id,
"emp_first_name": emp_first_name,
"emp_last_name": emp_last_name,
"emp_dob": emp_dob,
"emp_gender": emp_gender,
"emp_email": emp_email,
"emp_country": emp_country,    
"emp_salary": emp_salary    
}

print("\nEmployee Information in Dictionary Format: ")
print(employee_dict)