class X(object):
    pass

X.__class__
X.__class__.__base__

class Rectangle(object):
    def area(self) -> float:
        return self.length * self.width

