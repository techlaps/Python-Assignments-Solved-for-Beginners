employee_metadata_dict = {
"emp_id": "Enter Employee Id: ",
"emp_first_name": "Enter Employee First Name: ",
"emp_last_name": "Enter Employee Last Name: ",
"emp_dob": "Enter Employee DOB(date of birth in YYYY-MM-DD): ",
"emp_gender": "Enter Employee Gender: ",
"emp_email": "Enter Employee Email Address: ",
"emp_country": "Enter Employee Country: ", 
"emp_salary": "Enter Employee Salary: "
}

employee_dict = {}
    
for metadata_key, metadata_value in employee_metadata_dict.items():
    input_value = input(metadata_value)
    employee_dict[metadata_key] = input_value

print("\nEmployee Information in Dictionary Format: ")
print(employee_dict)