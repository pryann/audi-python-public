my_list = [10, 20, 30, 40, 50, 60]
sum_my_list = 0
for i in my_list:
    sum_my_list += i

print(sum_my_list)

my_list_2 = [345, 567, 23, 786479, 3, 234]
for i in my_list_2:
    sum_my_list += i

print(sum_my_list)


def say_hello(name):
    return 'Hello ' + name


say_hello('Gergő')
say_hello('Gizi')
print(say_hello('Gizi'))

hello_g = say_hello('Gergely')
print(hello_g)


def summarize_list_items(list_param):
    sum_list = 0
    for i in list_param:
        sum_list += i
    return sum_list


print(summarize_list_items([23, 456748, 264, 547]))
print(summarize_list_items([456, 46, 2, 5, 8, 9]))
my_num_list = [4, 6, 78, 32, 57]
print(summarize_list_items(my_num_list))


def avg_list_items(list_param):
    return summarize_list_items(list_param) / len(list_param)


print(avg_list_items([23, 456748, 264, 547]))
print(avg_list_items([456, 46, 2, 5, 8, 9]))

# { 'min': , 'max'}


def get_min_max(list_p):
    min_value = float('inf')
    max_value = -float('inf')
    for i in list_p:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    return {'min': min_value, 'max': max_value}

# minimum kiválasztás


def get_min(list_p):
    min_value = float('inf')
    for i in list_p:
        if i < min_value:
            min_value = i
    return min_value

# maximum kiválasztás


def get_max(list_p):
    max_value = -float('inf')
    for i in list_p:
        if i > max_value:
            max_value = i
    return max_value

# megszámlálás


def count_item(list_p, value):
    counter = 0
    for i in list_p:
        if i == value:
            counter += 1
    return counter

# eldöntés


def is_contain(list_p=[1, 2, 3], value=1):
    for i in list_p:
        if i == value:
            return True
    return False

    # print(get_min_max([1, 2, 3, 4, 5, 6]))
print(count_item([1, 2, 3, 4, 1, 2, 4, 3, 2, 3, 4, 3, 2], 2))
print(is_contain(value=10, list_p=[1, 2, 3]))
