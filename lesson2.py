# bài 2 kiểm tra tính chãn lẻ của số
def check_number(n):
    if n % 2 == 0:
        return "Đây là số chẵn"
    else:
        return "Đây là số lẻ"
try:
    number = int(input("Hãy nhập 1 số nguyên: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("lỗi")

