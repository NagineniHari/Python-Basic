# sample = ["server1","server2","server3","server4"]

# ## for, while

# ## Continue break

# value = 0

# """ 
# while value < 10 :
#     value = value + 1
#     print(value) 
    
#     """


# # while value < 10:
# #     if value == 5:
# #        break
# #     print(value)
# #     value = value + 1

# while value < 10:
#     if value == 5:
#        ## incrementing is very important
#        value = value + 1
#        continue
#     print(value)
#     value = value + 1

sample = ["server1","server2","server3","server4","675"]

# idx = 0

# while idx < len(sample):
#     print(sample[idx])
#     idx += 1  ## idx= idx + 1

## here idx is iterator
# Sample is  iterable
# for ele in sample: 
#     print(ele)

## In is membership operator (checks wether that element is present or not )
# print(1 in sample)
# print("server1" in sample)

## Access elements inside a list with  index using for loop

## print(ele) out side will not work only in for loop only its work

## Range,  enumerate
# print(list(range(5)))

# for idx in range(len(sample)): 
#     print(sample[idx])

# for idx in range(len(sample)): 
#     ele = sample[idx]
#     print(idx,ele)
print(enumerate(sample))
for idx,val in enumerate(sample):
    print(idx,val)

## tuple unpacking 

a, b = (1, 2)
print(a, b)

# while loop can be used when we know when to end
# for loop can be used when we don't know when to end

# consider a log file with n number of lines with w no: of words
# if both n as well w value is know, then we go for "while loop"
# if n and w are unknown then we go for "for loop"