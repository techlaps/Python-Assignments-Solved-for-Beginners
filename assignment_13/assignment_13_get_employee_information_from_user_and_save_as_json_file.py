# Import required python packages
import os
from os.path import join
import json

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

json_file_name = "employee_information.json"

with open(json_file_name, 'w') as file_object:    
    for metadata_key, metadata_value in employee_metadata_dict.items():
        input_value = input(metadata_value)
        employee_dict[metadata_key] = input_value
        
    json.dump(employee_dict, file_object)
        
json_file_location = join(os.getcwd(), json_file_name)
print("\nEmployee Information's JSON file location: {}".format(json_file_location))