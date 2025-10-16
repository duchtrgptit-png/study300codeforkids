# Chương trình in tất cả các số nguyên tố từ 1 đến 100
def check_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def print_number():
    for number in range(1,101):
        if check_number(number):
            print(number, end=' ')
        

print_number()