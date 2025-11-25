#057 - Viết chương trình để tìm giao của hai set
set_2 = set([1,2,3,4,5,3,2,1])
set_1 = {1, 3, 5, 6, 8, 1}
print(set_2.intersection(set_1))

set_giao = set_2 & set_1
print(set_giao)
