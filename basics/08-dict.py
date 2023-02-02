# Dictionary is a collection which is ordered ** and changeable. No duplicate members.

# - elérés kulcs alapján vagy a get() metódussal
# - keys() - kulcsokat adja vissza
# - values() - értékeket adja vissza
# - items() - kulcsokat és értékeket adja vissza
# - hozzáadás: thisdict["color"] = "red" vagy thisdict.update({"color": "red"})
# - pop() - eltávolítás kulcs alapján
# - copy() - másolás
# - dict() - dict-é konvertálás

my_dict = {'first': 'Gergely', 'last': 'Gáll'}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({'first': 'Zulu'})
print(my_dict)
my_dict.update({'age': 38})
print(my_dict)
my_dict.pop('first')
print(my_dict)
my_dict.update({'last': None})
print(my_dict['age'])
