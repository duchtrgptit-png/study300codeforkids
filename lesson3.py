# kiểm tra 3 số vừa nhận xem số nào lớn nhất
def check_three_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


try:
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))
    num3 = float(input("Nhập số thứ ba: "))
    result = check_three_number(num1, num2, num3)
    print(result)
except ValueError:
    print("Lỗi")
