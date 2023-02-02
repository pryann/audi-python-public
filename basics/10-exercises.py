import sys

my_list = [10, 20, 30, 40, 50, 60]
sum_my_list = 0
avg_my_list = 0

# for i in range(len(my_list)):
#     sum_my_list += my_list[i]

for i in my_list:
    sum_my_list += i

print(sum_my_list)
avg_my_list = sum_my_list / len(my_list)

print(avg_my_list)

reversed_my_list = []

# range paraméterezése fordítva
# append-el tudtok hozzáadni

# len(my_list) = 6, de a 6. elem indexe az 5
# range(0, 10) 0...9
# range(10, 0, -1) 10...1
#
for i in range(len(my_list) - 1, -1, -1):
    reversed_my_list.append(my_list[i])

print(reversed_my_list)
my_list.reverse()
print(my_list)

# max kiválasztás
maximum_value = 0
for i in my_list:
    if maximum_value < i:
        maximum_value = i

print(maximum_value)


# for i in range(0, len(my_list)):
#     print(f'index: {i}')
#     print(f'value: {my_list[i]}')

for i, v in enumerate(my_list):
    print(f'index: {i}', end=' ')
    print(f'value: {v}', end=' ')

print(float('inf'))
print(float('-inf'))

print('d' in ['a', 'b', 'c'])
