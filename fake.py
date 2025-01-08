# given a string 

name = 'Richard is amazing'

# amazing is richard

# no special chars
# single space

# ['Richard', 'is', 'amazing']

name = name.split(' ')

print(name)

print(type(name))

print(' '.join(name[::-1]))

