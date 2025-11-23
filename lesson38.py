#038 - Viết chương trình để đếm số lần xuất hiện của một phần tử trong tuple
tuple_2 = (3, 3, 3, 4, 4, 6, 35, 36, 67, 23)
print(f"Đây là tuple: {tuple_2}")
pt = int(input("Hãy nhập phần tử cần đếm: "))
if pt in tuple_2:
    print(f"{pt} xuất hiện:", tuple_2.count(pt), "lần")
else:
    print("Không tìm thấy phần tử")
    