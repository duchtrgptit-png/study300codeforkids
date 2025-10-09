# kiểm tra 3 số vừa nhận xem số nào lớn nhất
def find_max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
try:
    num1=float(input("Hãy nhập số thứ nhất: "))
    num2=float(input("Hãy nhập số thứ hai: "))
    num3=float(input("Hãy nhập số thứ ba: "))
    check = find_max_of_three(num1, num2, num3)
    print(f"{check} là số lớn nhất")
except ValueError:
    print("Không hợp lệ hãy thử lại")


