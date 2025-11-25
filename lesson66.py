#066 - Viết chương trình để đếm số lần xuất hiện của một ký tự trong chuỗi
name = 'hoàng trung đức'
kytu = input("Hãy nhập kí tự mà bạn muốn đếm: ")


if kytu in name:
    print(f"{kytu} xuất hiện: ",name.count(kytu))
else:
    print(f"{kytu} không có trong chuỗi")

    