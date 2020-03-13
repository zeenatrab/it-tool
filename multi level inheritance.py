# Program showing use of multilevel inheritance

# class 1


class Website:
        def first(self):
                print('freetimelearning.com')

# class 2


class Web2(Website):
        def sec(self):
                print('Busybee.com')
# class 3


class Web3(Web2):
        def final(self):
                print('hobby.com')
# creating object
a = Web3()
# calling function
a.first()
a.sec()
a.final()
