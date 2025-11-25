#072 - Viết chương trình để ghi nội dung vào một file văn bản
word = 'word.txt'

try:
    with open(word, 'w', encoding='utf-8') as file:
        write = file.write("Đặng Thị Hồng, Hoàng Trung Đức, Hoàng Tiến Đạt, Hoàng Văn Thái.")

except FileNotFoundError:
    print(f"Không tìm thấy file: {word}")
except Exception as e:
    print(f"Hiện đang bị lỗi: {e}")

