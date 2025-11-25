#054 - Viết chương trình để kiểm tra một phần tử có tồn tại trong set không
set_1 = {1, 3, 5, 6, 8, 1}
check = int(input("Hãy nhập 1 phần tử cần kiểm tra: "))
if check in set_1:
    print(f"Phần tử {check} có ở trong set")
else:
    print(f"Phần tử {check} không có ở trong set")
    