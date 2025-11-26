#079 - Viết chương trình để ghi thêm nội dung vào cuối file
words= 'word.txt'
try:
    with open(words, 'a', encoding='utf-8') as file:
        write = file.write('Hoàng Trung Đức')
        print(write)
except FileNotFoundError:
    print(f'Không tìm thấy file: {words}')
except Exception as e:
    print(f"Hiện đang bị lỗ: {e}")
    