def Find_UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return
try:
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhập số thứ hai: "))
    UCLN = Find_UCLN(num1, num2)
    print(f"Ước chung lớn nhất của {num1} và {num2} là : {UCLN}")

except ValueError:
    print("Lỗi")