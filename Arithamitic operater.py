# Creating arithamatic operator
class Arith:
    def calculate(self):
        selfx = int(input("Enter 1st no:"))
        selfy = int(input("Enter 2nd no:"))
        add = selfx + selfy
        sub = selfx - selfy
        mul = selfx * selfy
        div = selfx / selfy
        mod = selfx % selfy
        con = selfx + selfy
        print("addition is: %f" % (add))
        print("subtraction is: %f" % (sub))
        print("multiplication is: %f" % (mul))
        print("division is: %f" % (div))
        print("modulo is: %f" % (mod))
        print("concat is: %f" % (con)) 
# Creating object
c = Arith()
# Calling function
c.calculate()
s
