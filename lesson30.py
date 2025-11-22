#030 - Viết chương trình để đếm số lần xuất hiện của một phần tử trong danh sách
list = [1, 2, 3, 4, 2, 5, 76, 2, 4, 3, 7]
print(f"danh sách ban đầu: {list}")
pt_muon_dem = int(input("Nhập phần tử bạn muốn đếm trong danh sách: "))
if pt_muon_dem not in list:
    print("Không có số này")
else: 
    so = list.count(pt_muon_dem)
    print(f"{pt_muon_dem} xuất hiện: {so} lần")