# Chương trình tính tiền taxi dựa trên số km đã đi
def calculate_fare(km):
    if km <= 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km-1)*8500
    else:
        fare = 10000 + 9*8500 + (km-10)*7500
    return fare

try:
    distance = float(input("Hãy nhập số km bạn đã đi: "))
    if distance <= 0:
        print("Số km không hợp lệ!!")
    else:
        total_fare = calculate_fare(distance)
        print(f"Đây là tổng số tiền bạn phải trả: {total_fare}")
except ValueError:
    print("Không hợp lệ vui lòng thử lại")