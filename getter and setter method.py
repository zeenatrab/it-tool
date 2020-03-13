#  Program using getter and setter method


# Defining class Property_fun_demo
class Property_fun_demo:
    def __init__(self):
        self._age = 0

    # Function to get value
    def get_age(self):
        print("getter method called")
        return self._age

    # Function to set value
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # Function to delet age
    def del_age(self):
        del self._age
        # Calling property() function
        age = property(get_age, set_age, del_age)

# Creating object named as mark
mark = property_fun_demo()

# Passing arguement
mark.age = 10
print(mark.age)
