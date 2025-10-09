# bài 1 kiểm tra số âm hay số dương
def check_number(n):
    if n < 0:
        return "Đây là số âm"
    elif n > 0:
        return "Đây là số dương"
    else:
        return "Đây là số 0"
try:
    number = int(input("Hãy nhập số cần kiểm tra: "))
    result = check_number(number)
    print(result)
except ValueError: 
    print("Không hợp lệ, xin hãy thử lại.")