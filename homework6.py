my_dict = {'Vasya': 1995, 'Anna': 2004, 'Petr': 1992}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Valera'))
my_dict.update({'Valera':1976,
                'Mikhail':2012})
remove = my_dict.pop('Anna')
print(remove)
print(my_dict)
print("-----------------------------")
my_set = {1024, 'Computer', 3.14, (1, 2, 56,127),1024,1024,3.14, 'Computer'}
print(my_set)
my_set.add(55)
my_set.add(44)
my_set.remove(3.14)
print(my_set)