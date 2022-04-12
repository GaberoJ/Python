'''
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"], #random_dict["I"] = []
"М": ["Мария"],        #random_dict["I"].append('Ivan')
"П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?
'''

def thesaurus(*args):
    """Creates a dictionary with names."""
    dict_of_names = {}
    for name in args:
        if name[0] in dict_of_names:
            dict_of_names[name[0]].append(name)
        dict_of_names.setdefault(name[0], [name])
    dict_of_names = dict(sorted(dict_of_names.items()))
    return dict_of_names


if __name__ == "__main__":
    print(thesaurus("Иван", "Мария", "Петр", "Илья", "Афанасий", "Авдотья", "Кирилл", "Артур", "Павел"))
    
