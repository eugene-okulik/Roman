my_dict = {'tuple': (1, 'boundary', 2.54, True, None),
           'list': [1, 2, 'text', 1, 2.54],
           'dict': {1: 2, 2.5: 'text', 'strs': False, False: True, (1, 3): 'wsgsg'},
           'set': {3, 3, 4, 6, 2, 5}
           }

print(my_dict['tuple'][-1])

my_dict['list'].append(True)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 34
my_dict['dict'].pop(1)

my_dict['set'].add(34)
my_dict['set'].discard(3)
print(my_dict)
