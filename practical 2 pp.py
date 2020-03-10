# Iterables and iterators
print("----ITERABELS----")
# create a list
list1 = ["Mumbai", "Dheli", "Pune", "Patana"]
for city in list1:
    print(city)
    print("\n")

# Iterators
print("-----ITERATORS----")
iterator_obj = iter(list1)
try:
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
except:
    print("Stop Iteration Exception Raised")

