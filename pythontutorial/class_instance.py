from datetime import date
import pandas as pd
import os

here = os.path.dirname(os.path.abspath(__file__))

# defining constant mapping config for data table
NAME = 'Name'
ID = 'ID'
YOB = 'YOB'
ZIP_CODE = 'Zip Code'
SUPERVISOR_LEVEL = 'Supervisor Level'

# make the name read-only private to prevent acidental changes, but add method to read it
# zipcode is free to be changed outside the class
# class Person(object):
#     counter = 0 # class attribute
#     def __init__(self, name: str, zipcode: int): # instance attributes
#         self.__name = name
#         self._zipcode = zipcode
#         Person.counter += 1
#     def get_name(self): # instance method
#         return self.__name
#     def greet(self): # instance method
#         return f"Hi, it's {self.__name}."
    
#     @classmethod
#     def create_anonymous(cls):
#         return Person('Anonymous', 100100)


# PUBLIC, PROTECTED, PRIVATE VARIABLES
# Public and protected variables have no difference in actual restriction
# With the flag _, it just acts like a warning for other users not to change it 
# # outside the class or subclass
# class EmployeeOld(object):
#     company = 'ABC Pte. Ltd.'
#     company_size = 0
#     company_hq = 'Singapore'
#     def __init__(self, name: str = 'new_employee', id_number: int = '1111', birth_year: int = 1980, zip_code: int = '100100'):
#         self._name = name # protected variable
#         self._id_number = id_number
#         self._birth_year = birth_year
#         self.__zip_code = zip_code
#         self.__zip_code_history = [zip_code]
#         # self.__make_signature() # constructor broken up outside __init__()
#         self._signature = self.__make_signature() # alternative, still define the instance attribute within __init__

#         # self.company_size += 1 # incorrect as this only applies to the instance attribute
#         Employee.company_size += 1 # need to use the class name in front
#     def get_age(self):
#         return date.today().year - self._birth_year
#     def get_zip_code(self):
#         return self.__zip_code
#     def set_new_zip_code(self, new_zip_code: int):
#         self.__zip_code = new_zip_code
#         self.__zip_code_history.append(new_zip_code)
#         return('')
#     def get_zip_code_history(self):
#         return self.__zip_code_history 
#     # def __make_signature(self): # constructor broken up outside __init__()
#     #     self._signature = self._name + str(self._id_number) 
#     def __make_signature(self): # alternative
#         return self._name + str(self._id_number)
#     @classmethod
#     def change_company_hq(cls, new_hq: str):
#         Employee.company_hq = new_hq
#     @classmethod
#     def reset(cls):
#         cls.company_size = 0
#         cls.company_hq = 'Singapore'

class Pet(object):
    owner = 'John'
    address = '123 Highland Street'
    _default_name = 'petty'
    _default_pet_type = 'cat'
    pet_list = list()
    def __init__(self, name: str, pet_type: str):
        self._name = name
        self._pet_type = pet_type
        self.__class__.pet_list.append(self._name)
        # self.owner = Pet.owner
    def get_pet_signature(self):
        return (self._name + '-' + self._pet_type)
    def get_pet_owner_address(self):
        return Pet.owner + '-' + Pet.address
        # return self.owner + '-' + self.address
        # return cls.owner + '-' + cls.address
    @classmethod # use classmethod to create default object of the class, accessing class attributes
    def create_default_pet(cls):
        return Pet(cls._default_name, cls._default_pet_type)
    @classmethod
    def change_owner_1(cls, new_owner: str):
        cls.owner = new_owner
    # @classmethod
    # def change_owner_2(cls, new_owner: str):
    #     Pet.owner = new_owner

class Animal(Pet):
    pass
    
a1 = Pet('Mimi', 'cat')
a1.get_pet_signature()
a1.get_pet_owner_address()

a2 = Animal('Spiky', 'dog')
a2.get_pet_signature()
a2.get_pet_owner_address()

Pet.pet_list


print(a1.__class__)
print(a2.__class__)

if __name__ == '__main__':
    # employee_database = EmployeeDatabase(os.path.join(here, 'employees.csv'))
    # print(employee_database._employees_list[0]._object)
    # cat1 = Pet('Mimi', 'cat')
    # print('Instance attributes:')
    # print(cat1.address)
    # print(cat1.owner)
    # print(cat1._name)
    # print(cat1._pet_type)
    # print('Class attributes:')
    # print(Pet.owner)
    # print(Pet.address)
    print(Pet.__dict__)


# Employee.reset()

# p1 = Employee('John', 1234, 1993, 100200)
# p2 = Employee('David', 1244, 1990, 100500)
# p3 = Employee()
# s1 = Supervisor('Simon', 2234, 1970, 100999, 2)

# p1.company_size
# p1.company_hq
# p1._signature
# p1.get_age()
# s1._signature
# s1.get_zip_code_history()
# s1.set_new_zip_code(200999)
# s1.get_zip_code_history()

# # STATIC METHOD
# # no need any specific instances
# # used to group related functions together
# class TemperatureConverter:
#     @staticmethod
#     def celcius_to_fahrenheit(degc: float):
#         return 9 * degc / 5 + 32
    
#     @staticmethod
#     def fahrenheit_to_celcius(degf: float):
#         return 5 * (degf - 32) / 9


class Employee(object): # each row is an object, created by
    def __init__(self, attributes_list, values_list):
        self._attributes_list = attributes_list # column headers = keys
        self._object = dict(zip(attributes_list, values_list)) # key value pairs = main data structure to store object data
    def get_value_of_attribute(self, attribute=None): # handling wrong/empty input
        if attribute not in self._attributes_list:
            return None
        return self._object[attribute]
    def __str__(self): # str method for printing
        return "\n".join([f"{attribute}: {value}" for attribute, value in self._object.items()])

# SINGLE INHERITANCE
class Supervisor(Employee):
    def __init__(self, name: str, id_number: int, birth_year: int, zip_code: int, supervisor_level: int):
        super().__init__(name, id_number, birth_year, zip_code) # cannot specify types here, will inherit from parent class
        self._supervisor_level = supervisor_level


class EmployeeDatabase(object):
    def __init__(self, data_csv_table_path: str):
        self._employee_dataframe = self.__create_employee_dataframe(
            data_csv_table_path=data_csv_table_path)
        self._number_of_employees = len(self._employee_dataframe)
        self.__get_all_employee_info()
        self.__generate_employee_objects(
            employee_dataframe=self._employee_dataframe)

    def __create_employee_dataframe(self, data_csv_table_path):
        return pd.read_csv(data_csv_table_path)

    # the instance attribute is only produced when this method is invoked
    def __get_all_employee_info(self):
        self._employee_names = list(self._employee_dataframe[NAME])
        self._employee_ids = list(self._employee_dataframe[ID])
        self._employee_age = list(
            date.today().year - self._employee_dataframe[YOB])
        self._employee_zip_codes = list(self._employee_dataframe[ZIP_CODE])

    def __generate_employee_objects(self, employee_dataframe):
        self._employees_list = list()
        employee_attributes_list = list(employee_dataframe.columns)
        for row in employee_dataframe.values:  # for each ndarray of object
            employee_values_list = row.tolist()  # convert it to a list of mixed types
            # create Employee object for each record
            employee = Employee(
                attributes_list=employee_attributes_list, values_list=employee_values_list)
            self._employees_list.append(employee)
