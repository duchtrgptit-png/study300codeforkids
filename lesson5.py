#005 - Viết chương trình để tính điểm trung bình và xếp loại học sinh.

#Hàm tính toán:
def calculate_average(score):
    return sum(score) / len(score)

#hàm phân loại:
def classify_student(average):
    if average >= 8.5:
        return "Xuất sắc"
    elif average >= 7.0:
        return "Giỏi"
    elif average >= 5.5:
        return "Khá"
    elif average >= 4.0:
        return "Trung bình"
    else:
        return "Yếu"

#Hàm nhập dữ liệu từ người dùng:
try:
    scores = []
    subject = int(input("NHập số lượng môn học: "))
    if subject <= 0:
        print("Số môn học phải lớn hơn 0")
    else:
        for i in range(subject):
            score = float(input(f"Hãy nhập điểm của môn thứ {i+1}: "))
            if score < 0 or score > 10:
                print("Điểm môn học phải từ 0 đến 10")
                break
            scores.append(score)

        if len(scores) == subject:
            score_average = calculate_average(scores)
            classification = classify_student(score_average)
            print(f"Điểm trung bình: {score_average}")
            print(f"Xếp hạng: {classification}")
except ValueError:
    print("Không hợp lệ")
        

    
        


        
