def chu_vi_hinh_chu_nhat(d,r):
    return 2 * (d + r)
def dien_tich_hinh_chu_nhat(d,r):
    return d*r

try:
    cd = float(input("hãy nhập chiều dài: "))
    cr =float(input("hãy nhập chiều rộng: "))
    chu_vi = chu_vi_hinh_chu_nhat(cd,cr)
    dien_tich = dien_tich_hinh_chu_nhat(cd,cr)
    print(f"Đây là chu vi hình chữ nhật: {chu_vi}")
    print(f"Đây là diện tích hình chữ nhật:{dien_tich} ")
except ValueError:
    print("Lỗi")