people_list = [
    {'first': 'Gáll', 'last': 'Gergely', 'age': 38},
    {'first': 'Kiss', 'last': 'Gizi', 'age': 42, 'hobby': 'reading'},
    {'first': 'Blaha', 'last': 'Lujza', 'age': 66},
]

print(people_list[0]['last'])

# Név: Gáll Gergely
# Név: Kiss Gizi
# Név: Blaha Lujza

for i in range(len(people_list)):
    # print(i)
    print('Név:', people_list[i]['first'], people_list[i]['last'])
    print(f"Név: {people_list[i]['first']} {people_list[i]['last']}")

for i in range(len(people_list)):
    for j in people_list[i]:
        # print(i)
        print(people_list[i][j])
        # print(j)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

sum_matrix = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # sum_matrix = sum_matrix + matrix[i][j]
        sum_matrix += matrix[i][j]

print(sum_matrix)
