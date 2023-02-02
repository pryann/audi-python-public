# unique, "unchangeable"
my_set = {1, 2, 3, 1}
print(my_set)
# Error
# my_set[0] = 10
my_set.add(4)
print(my_set)
# remove random element
my_set.pop()
# remove a specific value
my_set.remove(2)
print(my_set)
my_set.add(1)
print(my_set)
print(my_set.issuperset({1, 2}))

my_str = 'abcdefgh'
print(my_str[0])
print('str: ', str(my_str))
print('list: ', list(my_str))
print('tuple: ', tuple(my_str))
print('set: ', set(my_str))

my_str_conv = list(my_str)
