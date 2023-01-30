from class_instance import here, EmployeeDatabase
import os
# no need to import Employee Class, 


if __name__ == '__main__':
    employee_database = EmployeeDatabase(os.path.join(here, 'employees.csv'))
    for employee in employee_database._employees_list:
        print(employee._object)
# def main():
#     employee_database = section1.EmployeeDatabase(os.path.join(section1.here, 'employees.csv'))
#     for employee in employee_database._employees_list:
#         print(employee._object)