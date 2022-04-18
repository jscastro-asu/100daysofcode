

# if num of values is unknown o
# tuple
def add(*args):
    sum_n =0
    for x in args:
       sum_n += x
    return sum_n       


#print(add(3, 4, 5, 2, 33, 3))

# use for keyword args
#dict
def calc(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
calc(add=2, subtract=6)