servers = ['192.168.145.23','192.168.145.24','192.168.145.25','192.168.145.26']

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

['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

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
server = [False,'192.168.145.23',True,'192.168.145.24',True,'192.168.145.25',False,'192.126.145.34',False]
server.remove(False)
print(server)

server = [s for s in server if s is not False]
server = [s for s in server if type(s) is not bool]

print(server)

server.reverse()
print(server)

server= server[::-1]
print(server)

server.sort()
print(server)

servers =[7,2,5,6,9,8,4,3,1]
## servers.sort()
## print(servers)

servers_1 = sorted(servers)
print(servers , servers_1)

servers = [False,'192.168.145.23',True,'192.168.145.24',True,'192.168.145.25',False,'192.126.145.34',False]
servers_1= servers.copy()
servers_1.remove(True)
print(servers , servers_1)