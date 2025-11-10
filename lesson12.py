while True:
    def sum_from_1_to_n(n):
        if n <0:
            return "vui lòng nhập 1 số nguyên lớn hơn 0"
        return (n * (n + 1))/2


    try:
        number = int(input("Hãy nhập vào 1 số nguyên: "))
        if number < 0:
            print("Hãy nhập 1 số lớn hơn 0")
        else:
            result = sum_from_1_to_n(number)
            print(f"Tổng từ 1 đến {number} là: {result}")
    except ValueError:
        print("Không hợp lệ vui lòng thử lại!!")

