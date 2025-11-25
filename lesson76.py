#075 - Viết chương trình để đếm số ký tự trong một file văn bản
import os
word = 'word.txt'
if os.path.isfile(word):
    print(f'file "{word}" tồn tại.')
else:
    print(f'file "{word}"không tồn tại.')