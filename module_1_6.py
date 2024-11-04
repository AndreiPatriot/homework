#1. Работа со словарями:
print('Работа со словарями:')
my_dict = {'Artem': 890537668589, 'Vladik': 89045565852, 'Gera': 86345788545 }
print(('Dict:'),my_dict)
print(('Existing value:'),my_dict['Vladik'])
print(('Not existing value:'),my_dict.get('Andrei'))
a =my_dict.pop('Gera')
print(('Deleted value:'), (a))
my_dict.update({'Aleksei': 89565256456352,
               'Sveta': 89645678956})
print(('Modified dictionary:'),my_dict)

#Работа с множествами:
print('Работа с множествами:')
my_set_ = [1,2,2,'Яблоко',56.896,]
my_set_ = set(my_set_)
print('Set:',my_set_)
print(my_set_.add(85))
print(my_set_.add('(5,16,87)'))
print(('Addendum:'),my_set_)
print(my_set_.remove('Яблоко'))
print('Removel:',my_set_)


