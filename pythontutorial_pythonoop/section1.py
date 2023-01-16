from datetime import date

# make the name read-only private to prevent acidental changes, but add method to read it
# zipcode is free to be changed outside the class
class Person(object):
    counter = 0 # class attribute
    def __init__(self, name: str, zipcode: int): # instance attributes
        self.__name = name
        self._zipcode = zipcode
        Person.counter += 1
    def get_name(self): # instance method
        return self.__name
    def greet(self): # instance method
        return f"Hi, it's {self.__name}."
    
    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 100100)

person = Person('John', 123456)

person._zipcode
# person._zipcode = 123457
# person._zipcode

# person.__name # attribute error

# person.get_name()
person.greet()

Person.counter
person.counter

person2 = Person('Jane', 112233)
person.counter

# PUBLIC, PROTECTED, PRIVATE VARIABLES
# Public and protected variables have no difference in actual restriction
# With the flag _, it just acts like a warning for other users not to change it 
# outside the class or subclass
class Employee(object):
    company = 'ABC Pte. Ltd.'
    company_size = 0
    company_hq = 'Singapore'
    def __init__(self, name: str, id_number: int, birth_year: int, zip_code: int):
        self._name = name # protected variable
        self._id_number = id_number
        self._birth_year = birth_year
        self.__zip_code = zip_code
        self.__zip_code_history = [zip_code]
        # self.company_size += 1 # incorrect as this only applies to the instance attribute
        Employee.company_size += 1 # need to use the class name in front
    def get_age(self):
        return date.today().year - self._birth_year
    def get_zip_code(self):
        return self.__zip_code
    def set_new_zip_code(self, new_zip_code: int):
        self.__zip_code = new_zip_code
        self.__zip_code_history.append(new_zip_code)
        return('')
    def get_zip_code_history(self):
        return self.__zip_code_history
    @classmethod
    def change_company_hq(cls, new_hq: str):
        Employee.company_hq = new_hq

p1 = Employee('John', 1234, 1993, 100200)
p2 = Employee('David', 1244, 1990, 100500)
p1.company_size
p1.company_hq

Employee.change_company_hq('Malaysia')
p1.company_hq

p1._name
p1._id_number
p1.get_age()
p1.get_zip_code()
p1.get_zip_code_history()
p1.set_new_zip_code(200200)
p1.get_zip_code()
p1.company

p2.company
p2.get_zip_code_history()
p2.set_new_zip_code(100600)
p2.get_zip_code_history()



# STATIC METHOD
# no need any specific instances
# used to group related functions together
class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(degc: float):
        return 9 * degc / 5 + 32
    
    @staticmethod
    def fahrenheit_to_celcius(degf: float):
        return 5 * (degf - 32) / 9


# SINGLE INHERITANCE
class Supervisor(Employee):
    def __init__(self, name: str, id_number: int, birth_year: int, zip_code: int, supervisor_level: int):
        super().__init__(name, id_number, birth_year, zip_code) # cannot specify types here, will inherit from parent class
        self._supervisor_level = supervisor_level
