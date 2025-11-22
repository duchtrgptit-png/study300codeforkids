#024 - Viết chương trình để xóa một phần tử khỏi danh sách
my_list = [1, 3, 4, 5, 7, 2]
try:
    delete = int(input("Hãy nhập phần tử muốn xóa"))
    if delete in my_list:
        my_list.remove(delete)
        print(f"Đây là danh sách sau khi xóa: {my_list}")
    else:
        print("Không tìm thấy phàn tử cần xóa")
except ValueError:
    print("Không hợp lệ")
