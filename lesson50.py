#050 - Viết chương trình để nối hai dictionary
dict_1 = {'key1':1 , 'key2': 2, 'key3': 3}
dict_2 = {'key5':5 , 'key6': 6, 'key7': 8}
#cách 1
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)

#cách 2
dict_4 = {**dict_1, **dict_2}
print(dict_4) 