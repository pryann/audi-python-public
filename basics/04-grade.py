grade = int(input('Add meg az érdemjegyet: '))

# if grade == 1:

# ha 1 elégtelen
# különben ha 2 elégséges
# különben ha 3 közepes
# különben ha 4 jó
# különben ha 5 jeles
# egyébként: Ez nem osztályzat

if grade == 1:
    print('elégtelen')
elif grade == 2:
    print('elégséges')
elif grade == 3:
    print('közepes')
elif grade == 4:
    print('jó')
elif grade == 5:
    print('jeles')
else:
    print('Ez nem osztályzat')
