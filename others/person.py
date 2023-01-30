from name import Name

class Person:
    def __init__(self, fname, lname, gender,dob):
        self.name = Name(fname, lname)
        self.gender = gender
        self.DOB = dob
    def get_name(self):
        return self.name.get_first_name() + " " + self.name.get_last_name()
    def get_gender(self):
        return self.gender

    def change_last_name(self,new_name):
        self.name.changeLastName(new_name)

    def get_dob(self):
        return self.DOB

if __name__ == "__main__":
    person = Person("John", "Brown", "Male",201107)
    print(person.get_dob())
    print(person.get_name())
    print(person.get_gender())
