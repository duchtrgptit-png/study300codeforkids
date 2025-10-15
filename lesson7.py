def year_test(year):
    if(year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0):
        return True
    else:
        return False
    
try: 
    year = int(input("Nhập năm cần kiểm tra: "))
    if year_test(year):
        print(f"Năm {year} là năm nhuận")
    else:
        print(f"Năm {year} không phải là năm nhuận")
except ValueError:
    print("Không hợp lệ vui lòng nhập lại")