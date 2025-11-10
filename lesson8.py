# hàm kiểm tra chẵn lẻ trong 1 list
def even_odd_check(numbers):
        odd = 0
        even = 0
        for number in numbers:
            if number % 2 == 0:
                even += 1
            else:
                odd += 1
        return even, odd



try:
    list = input("Hãy nhập vào danh sách các số nguyên: ")
    numbers = [int(number)for number in list.split()]
    even, odd = even_odd_check(numbers)
    print(f"Đây là tổng các số chẵn có trong danh sách:{even}")
    print(f"Đầy là tổng các số lẻ có trong danh sách:{odd}")
except ValueError:
    print("Hãy thử lại")
