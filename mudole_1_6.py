my_dict = {'Masha' : 1987, 'Denis' : 2000, 'Dima' : 2002, 'Anton' : 1999}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Olga'))
my_dict.update({'Boris': 1980, 'Roma': 1997})
a = my_dict.pop('Denis')
print(a)
print(my_dict)
my_set = {16, True, 'jet', 45.99, 'jet', 16, 88, 88, True}
print(my_set)
my_set.update({90, 'tou'})
print(my_set.discard(16))
print(my_set)