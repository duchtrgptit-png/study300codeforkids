#071 - Viết chương trình để đọc nội dung của một file văn bản
word = 'word.txt'

try:
    with open(word, 'r', encoding='utf-8') as file:#ending='utf-8'===> Giúp hiển thị văn bản tiếng việt
        content = file.read()
        print("Nội dung file:")

        print(content)

except FileNotFoundError:
    print(f'Không tìm thấy file: {word}')
except Exception as e:
    print(f"Hiện đang bị lỗi: {e}")
        
