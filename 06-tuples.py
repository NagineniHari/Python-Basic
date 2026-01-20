t = ()

t1 = tuple()

sample = ('192.168.145.23','192.168.145.24','192.168.145.25','192.168.145.26')
print(type(sample),sample)

##tuple is immutable
print(sample[0])

# sample[0] = 12

# print(sample)

# print(sample[0:2])

# print(sample[-1])

env_lists= ("DEV","QA","UAT","PREPROD","PROD")
##print(env_lists)
##  print(dir(env_lists))

"""
count ,index

"""

# sample = (1,2,5,5,3,4,4,5,5,6,9)
# sample.count(5)
# # print(sample.count(5)) ## 4
# # print(sample.count(15)) ## 0
# # print(sample.index(5))  ## 2

## Type casting : data types converstion

sample = ('192.168.145.23','192.168.145.24','192.168.145.25','192.168.145.26')
sample_l =list(sample)
print(type(sample_l))