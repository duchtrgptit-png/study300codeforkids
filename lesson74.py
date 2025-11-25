#074 - Viết chương trình để đếm số từ trong một file văn bản
words = 'word.txt'

try:
    with open(words, 'r', encoding='utf-8') as file:
        count_word = 0
        for letter in file:
            words = letter.split()
            count_word += len(words)
            print(f"Số lượng từ có trong file là: {count_word}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {words}")
except Exception as e:
    print(f"Hiện đang bị lỗi: {e}")