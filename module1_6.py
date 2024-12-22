my_dict = {'Vlad': 1998, 'Dasha': 1990, 'Alex': 1988}
print("Dict:", my_dict)
print("Existing value:", my_dict ['Dasha'])
Not_existing_value = my_dict.get('Kostya')
print("Not existing value:", Not_existing_value)
my_dict ['Sasha'] = 2001
my_dict ['Anya'] = 1993
print("Deleted value:", my_dict['Vlad'])
del my_dict ['Vlad']
print("Modified dictionary :", my_dict)
print('\n')
my_set = {2, 3, 3,'Fox', 2, 4.4, 3, 77}
print("Set:", my_set)
my_set.add(11.11)
my_set.add('Window')
my_set.discard('Fox')
print("Modified set:", my_set)