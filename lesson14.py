def find_max_in_list(numbers):
    if not numbers:
        return "Danh sách rỗng, vui lòng nhập số"
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            num = max_number
    return max_number
try:
    input_number = input("hãy nhập vào 1 danh sách")
    numbers = [float(number) for number in input_number.split() ]
    if not numbers:
        print("Danh sách rỗng")
    else:
        max_number = find_max_in_list(numbers)
        print(f"{max_number} là số lớn nhất trong danhh sách")
except ValueError:
    print("Không hợp lệ vui lòng thử lại")

