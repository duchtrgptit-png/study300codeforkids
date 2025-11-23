#037 - Viết chương trình để kiểm tra một phần tử có tồn tại trong tuple không
list_1 = [1, 3, 4, 5, 2, 3, 8]
print(list_1)
pt = int(input("Hãy nhập phần tử cần tìm: "))
if pt in list_1:
    print(f" phần tử {pt} có ở trong danh sách")
else:
    print("Không tìm thấy phần tử")