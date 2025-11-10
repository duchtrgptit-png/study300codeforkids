# chuỗi palindrome là 1 chuỗi có thể gồm số hoặc chữ khi viết ngược hay xuôi đều giống nhau
while True:    
    def is_palindrome(n):
        n = "".join(char.lower() for char in n if char.isalnum())
        return n == n[::-1]
    try:
        input_string = input("Nhập vào 1 chuỗi: ")
        if is_palindrome(input_string):
            print(f"{input_string} là 1 chuỗi palindrome")
        else:
            print(f"{input_string} không phải là 1 chuỗi palindrome")
    except ValueError:
        print("Không hợp lệ vui lòng thử lại")