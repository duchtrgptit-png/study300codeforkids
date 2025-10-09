# Chương trình tính tiền taxi dựa trên số km đã đi
def calculate_fare(km):
    if km <= 1:
        fare = 20000
    elif km <= 10:
        fare = 20000 + (km-1) * 9000
    else:
        fare = 20000 + 9*9000 + (km-10)* 7000
    return fare
try:
    distance = float(input("Hãy nhập số km bạn đã đi: "))
    if distance <= 0:
        print("Số km không hợp lệ xin hãy thử lại")
    else:
        total = calculate_fare(distance)
        print(f"{total} là số tiền bạn cần trả")
except ValueError:
    print("Không hợp lệ hãy nhập lại")
