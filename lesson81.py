#081 - Viết chương trình để tạo một lớp học sinh
class student:
    def __init__(self, name, age, aver_scores):
        self.name = name 
        self.age = age
        self.aver_scores = aver_scores
    def show_info(self):
        print(f'Tên: {self.name}')
        print(f"Tuổi: {self.age}")
        print(f"Điểm trung bình: {self.aver_scores}")
    def classification(self):
        if self.aver_scores >= 9.0:
            return "Xuất sắc"
        elif self.aver_scores >= 8.0:
            return "Giỏi"
        elif self.aver_scores >6.5:
            return "Khá"
        elif self.aver_scores >= 3.5:
            return "Trung bình"
        else:
            return "Yếu"
st = student("Hoàng Trung Đức", 19, 9.2)
st.show_info()
print(f"Xếp loại: {st.classification()}")