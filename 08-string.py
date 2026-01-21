sample = "Hello, How are you doing ,how is devops course is any thing PENDING STATUS"
sample_1 ="abc" ## ("a","b","c")
# print(sample[8])
# print(sample_1[0])
## print(dir(sample))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill'

"""

print(sample.casefold()) ## change all small letters in the string

print(sample.center(100))

print(sample.center(100,"#"))


## Reverse String 

print(sample[::-1])  ## it's show the reverse string
print(tuple(sample_1), list(sample_1))

sample = "Hello, How are you doing ,how is devops course is any thing PENDING STATUS"
print(sample.split(" "))

print("#".join(sample.split(" ")))

## concatenations   joining 2 strings

print("a"+"b")


## How do you print a file path
# print("D:\DevOps\daws-86s\Project-Repo\Python-Basic\08-string.py")

# print(r"D:\DevOps\daws-86s\Project-Repo\Python-Basic\08-string.py")

# print(r"D:\\DevOps\\daws-86s\\Project-Repo\\Python-Basic\\08-string.py")
