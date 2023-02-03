num = 10
num_2 = num

print(num, num_2)

num = 20

print(num, num_2)


def do_something(num_param):
    num_param = 0
    return num_param


print(do_something(num), num)


my_list = [1, 2, 3, 4]
my_list_2 = my_list
print(my_list, my_list_2)

my_list.append(5)
print(my_list, my_list_2)
my_list_2.append(6)
print(my_list, my_list_2)
my_list_3 = my_list.copy()  # my_list[:]
my_list_2.append(7)

print(my_list, my_list_3)


def do_something_2(list_param):
    # NE CSINÁLD!
    # list_param.append(10)
    list_param.clear()
    list_param.extend(['Egy', 'Kettő'])
    return list_param


print(my_list)
do_something_2(my_list)
print(my_list)


def do_something_3(list_param):
    pass


def normalize_data(d):
    return 'norm'


data = 'data'
normalized_data = normalize_data(data)
