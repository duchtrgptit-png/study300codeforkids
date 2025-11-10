# 015 - Viết hàm để tính tổng các chữ số của một số
def sum_in_a_number(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
try:
    number = int(input("Hãy nhập vào 1 số nguyên: "))
    result = sum_in_a_number(number)
    print(f'Tổng của {number} là: {result}')
except ValueError:
    print("Giá trị không hợp lệ vui lòng thử lại")
