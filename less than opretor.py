# Python program to overload equality
# and less than operators


class A:
    def __init__(self, a):
        self.a = a

    # creating less than operator
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob1 is greater than ob2"
            
    def __eg__(self, other):
        if(self.a < other.a):
            return "Both are equal"
        else:
            return "Not equal"
# Creating object
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)
