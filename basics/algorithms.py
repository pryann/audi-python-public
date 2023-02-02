# Összegzés

def summarize(values):
    sum_value = 0
    for value in values:
        sum_value += value
    return sum_value


val = [10, 20, 30, 40, 50]

print(summarize(val))
print(sum(val))


# Megszámlálás - adott elem hányszor van benne

def count_values(values, search):
    counter = 0
    for value in values:
        if (value == search):
            counter += 1
    return counter


print(count_values(val, 10))
print(val.count(10))

# Minimum kiválasztás


def minimum(values):
    min_value = values[0]
    for index in range(1, len(values)):
        if values[index] < min_value:
            min_value = values[index]
    return min_value


print(minimum(val))
print(min(val))

# Maximum kiválasztás


def maximum(values):
    max_value = values[0]
    for index in range(1, len(values)):
        if values[index] > max_value:
            max_value = values[index]
    return max_value


print(maximum(val))
print(max(val))


# Eldöntés - True, False

def contains_or_not(values, search):
    for value in values:
        if value == search:
            return True
    return False


print(contains_or_not(val, 10))
print(10 in val)

# Kiválasztás - tudjuk, hgoy benne van, az index kell


def get_index(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index


print(get_index(val, 20))
print(val.index(20))

# Lineáris keresés - adjuk vissza az idnexet, ha benne van


def linear_search(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index
    return -1


print(get_index(val, 20))
print(val.index(20))
