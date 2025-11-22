import math
def chu_vi_hinh_tron(r):
    return 2 * math.pi * r
def dien_tich_hinh_tron(r):
    return math.pi * r * r


try:
    ban_kinh = float(input("Hãy nhập bán kinh: "))
    if ban_kinh < 0:
        print("Bán kính phải lớn hơn 0")
    else:
        chu_vi = chu_vi_hinh_tron(ban_kinh)
        dien_tich = dien_tich_hinh_tron(ban_kinh)
        print(f"Đây là chu vi của hình tròn: {chu_vi:.2f}")
        print(f"Đây là diện tích của hình tròn: {dien_tich:.2f}")
except ValueError:
    print("Lỗi")

    