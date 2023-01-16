import section1
import os

if __name__ == '__main__':
    employee_database = section1.EmployeeDatabase(os.path.join(section1.here, 'employees.csv'))
    print(employee_database._employees_list[0]._object)