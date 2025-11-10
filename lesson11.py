def giai_thua(n):
    if n < 0:
        return "giai thừa của 1 số phải lớn hơn 0"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)
    
try:
    number = int((input("Hãy nhập số cần tính: ")))
    if number < 0:
        print("Hãy nhập số lớn hơn 0")
    else:
        print(f"giai thừa của {number} là: {giai_thua(number)}")
    
except ValueError:
    print("Không hợp lệ, vui lòng thử lại")
    