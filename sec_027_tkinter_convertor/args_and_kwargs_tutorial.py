# def add(*args): # *args is converted into tuple
#     sum = 0
#     for n in args:
#         sum = n + sum
#     return sum

# print(add(2,5,6,11))





# def calculate(**kwargs):    # key:word arguments - dictionary
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
       
# calculate(add=3, multiply=5)





# def calculate(n, **kwargs):    # key:word arguments - dictionary
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"] 
#     print(n)
    
# calculate(3, add=3, multiply=5)





class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]    # must be defined in my_car = Car() , during inicialization
        self.seats = kw.get("seats")   # doesn't have to be defined in my_car = Car() , during inicialization 
        self.color = kw.get("color")
        
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)