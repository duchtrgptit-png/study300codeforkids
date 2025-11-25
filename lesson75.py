#075 - Viết chương trình để đếm số ký tự trong một file văn bản
words = 'word.txt'
try:
    with open(words, 'r', encoding='utf-8') as file:
        char_count = 0
        content = file.read()
        filtered_content = ''.join(c for c in content if c not in (" ", "\n", "\t"))
        char_count += len(filtered_content)
        print(f"Tổng số kí tự trong file là: {char_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {words}")
except Exception as e:
    print(f"Hiện đang bị lỗi: {e}")
    