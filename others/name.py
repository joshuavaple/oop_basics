class Name:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def get_first_name(self):
        return self.fname

    def get_last_name(self):
        return self.lname
    
    def change_last_name(self,newname):
        self.lname = newname

    def __repr__(self):
        return f"fname={self.fname};lname={self.lname}"


# testing code:
# if __name__ == "__main__":
#     name = Name("Jordan","Williams")
#     print(name)

# without above syntax, testing codes will be executed
# when the module is imported elsewhere
name = Name("Jordan","Williams")
print(name)