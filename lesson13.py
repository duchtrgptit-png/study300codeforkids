while True:    
    def so_nguyen_to(n):
        
        if n <= 1:
            return False
        elif n == 2 or n == 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i ==0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    try:
        number = int(input("Hãy nhập số nguyên để kiểm tra: "))
        if number <= 0:
            print("Hãy nhập 1 số lớn hơn 0")
        else:
            result = number
            if so_nguyen_to(result):
                print(f"{result} là số nguyên tố")
            else:
                print(f"{result} không phải là số nguyên tố")
    except ValueError:
        print("Giá trị không hợp lệ vui lòng thử lại!!")
