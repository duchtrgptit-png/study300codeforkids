#029 - Viết chương trình để tính tổng các phần tử trong danh sách
import random
list = [random.randint(1,100) for _ in range(10)]
print(list)
my_list = sum(list)
print(my_list)