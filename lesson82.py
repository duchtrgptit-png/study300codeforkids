#082 - Viết chương trình để thêm thuộc tính cho lớp học sinh
class student:
    def __init__(self, name, age, aver_scores, address):
        self.name = name
        self.age = age
        self.aver_scores = aver_scores
        self.address = address
    def show_info(self):
        print(f'Tên: {self.name}')
        print(f"Tuổi: {self.age}")
        print(f"Điểm trung bình: {self.aver_scores}")
        print(f'Địa chỉ: {self.address}')
    def classification(self):
        if self.aver_scores >= 9.0:
            return 'Xuất sắc'
        elif self.aver_scores >= 8.0:
            return "Giỏi"
        elif self.aver_scores >= 6.5:
            return "Khá"
        elif self.aver_scores >= 3.5:
            return "Trung bình"
        else:
            return "Yếu"
st = student("Hoàng Trung Đức", 19,9.2,"Khu 5, thị trấn Cái Rồng, Vân Đồn, Quảng Ninh")
st.show_info()
print(f'Xếp loại: {st.classification()}') 
