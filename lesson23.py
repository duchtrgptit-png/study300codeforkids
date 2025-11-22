#023 - Viết chương trình để thêm một phần tử vào đầu danh sách
list = ["cat", "dog", "bird", "swan"]
extra = input("Hãy nhập phần tử muốn thêm: ")
list.insert(0, extra)
print(list)