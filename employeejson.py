# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

# import json
# {'name': 'Madhu', 
#   'dob': '23-11-1998', 
#   'height': '5.1', 
#   'city': 'Kota', 
#   'state': 'Rajasthan'
#   }
# {'name': 'Abhiram', 
#  'dob': '12-7-1992', 
#  'height': '5.2', 
#  'city': 'Jaipur', 
#  'state': 'Rajasthan'
#  }
# {'name': 'Swathi', 
#  'dob': '19-11-1995', 
#  'height': '4.9', 
#  'city': 'Jodhpur', 
#  'state': 'Rajasthan'
#  }
# {'name': 'Harika', 
#   'dob': '23-1-1997', 
#   'height': '4.8', 
#   'city': 'Ajmer', 
#   'state': 'Rajasthan'
#  }
# {'name': 'Dileep', 
#  'dob': '29-10-1998', 
#  'height': '4.9', 
#  'city': 'Udaipur', 
#  'state': 'Rajasthan'
#  }



# For creating a json file of 5 employees and print objects of Employee class in list-->

import json

class Employee:
    def __init__(self):
        self.emp_dic = {}

    def create_employee(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input("Enter your DOB: ")
            height = input("Enter your height: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            emp = {'name': name, 'dob': dob, 'height': height, 'city': city, 'state': state}
            emp_id = len(self.emp_dic) + 1
            self.emp_dic[emp_id] = emp
        with open("emps.json", "w") as f:
            json.dump(self.emp_dic, f)

    def data(self):
        emp_list = []
        with open("emps.json", "r") as f:
            data = json.load(f)
        for emp in data.values():
            emp_list.append(emp)
        print(emp_list)

x = Employee()
x.create_employee()
x.data()

