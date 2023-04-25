import json
import random


emp_names = ["Ganesh", "Ganesh reddy", "M Ganesh", "Ganesh Magasani", "Magasani Ganesh", "Ganesh Kumar Reddy", "Ganesh Narayana Reddy"]
emp_ages = [18, 19, 20, 21, 22, 23, 24]
emp_salarys = [1000, 10000, 20000, 30000, 40000, 50000, 60000]
emp_addresses = ['Tirupati', 'Madanapalle', 'Chennai', 'MPL', 'Tirumala', 'TTD', "Chittoor"]
print("updated")
print("updated2")

def lambda_handler(event, context):
    # TODO implement
    try:
        randam_index = random.randint(0, 6)
        mock_data = {}
        mock_data['emp_name'] = emp_names[randam_index]
        mock_data['emp_age'] = emp_ages[randam_index]
        mock_data['emp_salary'] = emp_salarys[randam_index]
        mock_data['emp_addresses'] = emp_addresses[randam_index]
        print(mock_data)
        return mock_data
    
    except Exception as e:
        print(e)
