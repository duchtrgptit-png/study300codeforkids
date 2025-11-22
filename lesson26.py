#026 - Viết chương trình để sắp xếp danh sách theo thứ tự giảm dần
import random
list = [1, 2, 3, 4, 2, 5, 76, 2, 4, 3, 7]
random.shuffle(list)
print(f"Đây là danh sách bị xáo trộn: {list}")
list1 = list.copy()
list1. sort(reverse=True)
print(f"đây là danh sách sắp xếp theo thứ tự giảm dần: {list1}")
