#  It adds the numbers inside the function

# *args and **kwargs
# args - Extra values (positional)

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1, 2, 3, 4))



# **kwargs - Extra values with names

def user_detals(**info):
    print(info)
    
user_detals(name = "aditya", adge = 22)