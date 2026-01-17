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

