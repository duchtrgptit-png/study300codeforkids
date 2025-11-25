import os
word = 'words.txt'
try:
    with open(word, 'r', encoding='utf-8') as file:
        if os.path.isfile(word):
            os.remove(word)
            print(f"Đã xóa file: {word}")
        else:
            print(f"Không tìm thấy file cần xóa")
except FileNotFoundError:
    print(f"Không tìm thấy file cần tìm: {word}")
except Exception as e:
    print(f"Đang bị lỗi: {e}")
