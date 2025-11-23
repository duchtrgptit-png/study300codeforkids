#044 - Viết chương trình để xóa một cặp key-value khỏi dictionary
my_dict = {'name': 'duc', 'age': 18, 'country': 'VN'}
del(my_dict['name'])
print(my_dict)
my_dict.pop('age')
print(my_dict)