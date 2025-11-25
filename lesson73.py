#073 - Viết chương trình để đếm số dòng trong một file văn bản
word = 'word.txt'
try:
    with open(word, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
        print(f"Số lượng dòng trong file: {line_count}")
except FileNotFoundError:
    print(f'Không tìm thấy file: {word}')
except Exception as e:
    print(f'Hiện đang bị lỗi: {e}')