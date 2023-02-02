my_tuple = (1, 2, 3, 1)
print(my_tuple)

print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(1))

for i in my_tuple:
    print(i)

# Error
# my_tuple[0] = 0

i = 10
while i > 0:
    print(i)
    i = i - 1

my_num = 67
while True:
    user_num = int(input('Gondoltam egy számra 1 és 100 között, tippelj: '))
    if my_num == user_num:
        print('Talált')
        break
    elif user_num > my_num:
        print('Kissebbre gondoltam')
    elif user_num < my_num:
        print('Nagyobbra gondoltam')

    # amíg nem találta ki a számot:
    #     kérj be egyet
    #     ha eltalta írd ki, hogy eltaláltad
    #     ha kisebb, mint amire gondoltam, írd ki, hogy nagyobbra gondoltam
    #     ha nagyobb, mint amire gondoltam, írd ki, hogy kisebbre gondoltam

my_tuple_2 = (1, 2, 3)
my_tuple_2 = (4, 5, 6)
