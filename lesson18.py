def celsius_to_Fahrenheit(n):
    F = (n * 1.8) + 32
    return F
try:
    Celsius = float(input("Hãy nhập độ C cần đổi: "))
    result = celsius_to_Fahrenheit(Celsius)
    print(f"{Celsius} độ C đổi ra được {result} dộ F")
except ValueError:
    print("Giá trị không hợp lệ vui lòng thử lại")