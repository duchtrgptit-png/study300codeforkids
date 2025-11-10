
def power_function(a, b):
    return a ** b

try:
    co_so = float(input("Hãy nhập cơ số: "))
    so_mu = float(input("Hãy nhập vào số mũ: "))
    result = power_function(co_so, so_mu)
    print(f"Lũy thừa của {co_so} mũ {so_mu} là: {result}")
except ValueError:
    print("Giá trị không hợp lệ vui lòng thử lại!!")
