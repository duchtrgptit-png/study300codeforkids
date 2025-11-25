word = 'word.txt'
try:
    with open(word, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print(f'Không tìm thấy file: {word}')
except Exception as e:
    print(f"Hiện đang bị lỗi: {e}")