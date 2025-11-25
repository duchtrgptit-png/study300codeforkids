#056 - Viết chương trình để tìm hợp của hai set
set_2 = set([1,2,3,4,5,3,2,1])
set_1 = {1, 3, 5, 6, 8, 1}
print(set_2.union(set_1))

set_union = set_1 | set_2
print(set_union)
