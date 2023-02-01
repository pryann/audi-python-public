my_list = [34, 45, 56, 12.12, True, 'str', None, 34]
# get
print(my_list[0])
# print(my_list[10])
print('End of code')

my_prices = [1234, 1335345, 346547, 346576, 2354]
standard_hungarian_tax_rate_in_percent = 27
print('Lista hossza: ', len(my_prices))

# for - léptetős ciklus
# i - ciklusváltozó
# belül a ciklusmag
# range: mettől, meddig, lépésköz
for i in range(5, 15, 3):
    print(i)

for i in my_prices:
    print(i * (1 + standard_hungarian_tax_rate_in_percent / 100))

for i in range(len(my_prices)):
    print(my_prices[i])

my_number_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# slicing
print(my_number_2[2:4])   # [3, 4] 3-től 4. indexig
print(my_number_2[2:])    # [3, 4, 5, 6, 7, 8, 9] második indextől
print(my_number_2[:2])    # [1, 2] második indexig
print(my_number_2[2:7:2])  # [3, 5, 7] másodiktól, hatodikig, kettesével
print(my_number_2[2::2])  # [3, 5, 7, 9] másodiktól kettesével
print(my_number_2[-1])    # utolsó elem

# update
my_number_2[0] = 'Egy'
print(my_number_2)

for i in range(1, len(my_number_2)):
    my_number_2[i] = my_number_2[i] * 2
print(my_number_2)

# append - hozzáadás a végéhez
my_number_2.append(1000)
print(my_number_2)
# pop- utolsó elem törlése
my_number_2.pop()
print(my_number_2)

my_number_2.remove('Egy')
print(my_number_2)
