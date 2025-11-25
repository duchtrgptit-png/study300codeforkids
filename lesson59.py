#059 - Viết chương trình để xóa tất cả các phần tử trong set
set_2 = set([1,2,3,4,5,3,2,1])
#print(set_2.clear())

for items in list(set_2):
    print(set_2.remove(items))
