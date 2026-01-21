# def func_name():
#     print("Hello Python")

# #func_name()
# print(func_name())


# def mult(a,b):
#     return a * b ## Default is none 

# res = mult(9,8)
# print(res)

# def mult(a:int, b:int) -> int:
#     return a * b ## Default is none 

# res = mult(9.0,4)
# print(res)

# def mult(a, b , *args, **kwargs) :
#     ## *args -> pass any number: of position argements
#     ## *kwargs -> pass any number: of keywords argements
#     print(f"a:{a},b:{b} ,c:{args},d:{kwargs}")
#     return a * b ## Default is none 

# ## a=3, b=2 are keyword arguments ,as they contains keys and values
# ## '9.0' , 4 are called as positional arguments
# res = mult('9.0' , 4, 3, 2,c=20,d=40)
# print(res)

"""
When we specify data type in function but if we give different data type when passing the values what happen
"""

# def abc(a:int, b:float) -> float:
#     return a + b
# print(abc(1, 2.0))


def calc(a, b, operation):
    if operation == "add" :
       return a + b
    if operation == "sub" :
        return a - b
    if operation == "mult" :
        return a * b
    if operation == "div" :
        return a % b
values = tuple(input(" Enter two numbers: "))
operation = input( "Enter operation to perform(add,sub.mult,div): ")
print(values)
map(values, int)
res = calc(values, operation)