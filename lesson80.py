word1 = 'word.txt'
word2 = 'word2.txt'
try:
    with open(word1, 'r', encoding='utf-8') as source_file:
        content = source_file.read()
    with open(word2, 'w',encoding='utf-8') as destination_file:
        destination_file.write(content)
    print(f"Nội dung đã được sao chép từ: {word1} sang {word2}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {word1}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {word2}")
except Exception as e:
    print(f'Hiện đang bị lỗi: {e}')
