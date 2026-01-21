

print({'a','b','a'})

sample={'a','b','a'}

# Sets are an unordered collection
# Sets removed duplicates values and stored unique values
sample = set() ##{}

# print(dir(set()))

"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

"""
sample.add(10)
print(sample)

## Print(sample[0])  ## set is not worked here
## Ordered Collections (such as list, tuple, dict) supports indexing
## Unordered Collections does't support indexing

S1 = {1, 2, 3, 4}
S2 = {2, 4, 6, 8}
print(S1.difference(S2))
S1.difference_update(S2)
print(S1)