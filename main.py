from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

tel_pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\(]*(доб.)*[\s]*(\d+)*[\)]*"
tel_sub = r"+7(\2)\3-\4-\5 \6\7"

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ


def first_function(contacts_list):
    result_list = []
    for item in contacts_list:
        a = " ".join(item)
        b = a.split(" ")
        phone = re.sub(tel_pattern, tel_sub, item[5])
        result = [b[0], b[1], b[2], item[3], item[4], phone, item[6]]
        result_list.append(result)
    return second_function(result_list)


def second_function(result_list):
    contacts = {}
    for items in result_list:
        if items[0] in contacts:
            item_value = contacts[items[0]]
            for i in range(len(item_value)):
                if items[i]:
                    item_value[i] = items[i]
        else:
            contacts[items[0]] = items
    return list(contacts.values())


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(first_function(contacts_list))
