server_1 = "192.168.145.23"
server_2 = "192.168.145.24"
server_3 = "192.168.145.25"
server_4 = "192.168.145.26"

servers = ['192.168.145.23','192.168.145.24','192.168.145.25','192.168.145.26']
## print(servers)

## python is zero based indexing start 0,1 ..
server_2 = servers[3]
## print('server 2 IP Address:', server_2)

## Slicing (start indexing : end indexing ) end indexing is not including if you want end index you can mention end indexing +1
simple_slice = servers[0:3]
## print(simple_slice)

## Slicing (step sizes)
servers = ['192.168.145.23','192.168.145.24','192.168.145.25',
           '123456','192.168.145.27','192.168.145.28','192.168.145.29','192.168.145.30',
           '192.168.145.31','192.168.145.32','192.168.145.33',False,'192.1268.145.34']
simple_step_slice = servers[0:9:2]  ## step sizes  1, 1+2, 3+2, 5+2, 7+2
### print(simple_step_slice)

## Negative indexing
simple_step_slice = servers[-1:-3:-1]
### print(simple_step_slice)

### print("Length of list:",len(simple_step_slice))

## List of datatypes in python (list is mutable datatype) 
# Mutable datatype: Once defined,can change at any time eg: list,dictonaries
# Immutable datatype: Once defined,can't be changed  eg: Tuple,sets

## print(servers)
servers[3] = 123456789 ## Inplace operation
## print("after modification:", servers)

### print("list of operations:",dir(servers))

"""
list of operations:
 ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""

servers.append(False)
print(servers)

servers.append(["a","b","c"])

print("after append:",servers ,len(servers))


## multiple sizing or Multi indexing

servers[-1][0]
print(servers[-1][1])

servers.extend(["a","b","c"])

print(servers)

print("after extend:",servers ,len(servers))

print(servers.index(False))

servers.insert(0,10)
print(servers)

servers.remove(False)
print(servers)