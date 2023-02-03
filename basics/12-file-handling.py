import csv

# with open('files/survey_light.csv', encoding='utf-8') as csv_file:
#     content = csv.reader(csv_file, delimiter=',')
#     language_count = 0
#     language = 'Python'
#     for row in content:
#         languages = row[1].split(';')
#         if language in languages:
#             language_count += 1

# print(language_count)

# Feladat: készítsd egy függvényt, ami paraméterként kapja meg a file útvonalát,
# és azt melyik nyelvet keressük
# A Visszatérési érték a nyelv darabszáma


def get_language_count(path, language):
    with open(path, encoding='utf-8') as csv_file:
        content = csv.reader(csv_file, delimiter=',')
        lang = language.lower()
        language_count = 0
        for row in content:
            languages = row[1].lower().split(';')
            if lang in languages:
                language_count += 1
    return language_count


print(get_language_count('files/survey_light.csv', 'python'))
