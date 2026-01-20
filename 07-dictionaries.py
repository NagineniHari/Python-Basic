d = {}

d_1 = dict()


sample = {'a':1, 'b':2}

print(sample['a'],sample.get('b'))

## Dictionaries are mutable datatypes in python
sample['a'] = 20

print(sample['a'],sample.get('b'))

## Keys in Dictionaries once define can't be cahnged those are immutable 

samples ={("a","b"):10 ,'c':30}
print(samples)

## print(dir(dict))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

"""

print(sample.keys(), sample.values())

print(samples.keys(), samples.values())

sample_list= [({'a','b'},1) ,('c',2)]

print(sample_list)

## Type casting
sample_dict = dict(enumerate(sample_list))
print(sample_dict)
