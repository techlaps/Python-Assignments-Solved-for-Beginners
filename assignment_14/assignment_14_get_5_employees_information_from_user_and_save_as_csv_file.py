# Import required python packages
import os
from os.path import join
import csv

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

csv_file_name = "5_employees_information.csv"

with open(csv_file_name, 'w') as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerow(employee_metadata_dict.keys())
    
    for i in range(5):
        employee_info = []
        for metadata_key, metadata_value in employee_metadata_dict.items():
            input_value = input(metadata_value)
            employee_info.append(input_value)

        writer_object.writerow(employee_info)
        
csv_file_location = join(os.getcwd(), csv_file_name)
print("\nEmployees Information's CSV file location: {}".format(csv_file_location))