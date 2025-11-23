#045 - Viết chương trình để kiểm tra một key có tồn tại trong dictionary không
my_dict = {'name': 'duc', 'age': 18, 'country': 'VN'}
key = input("Hãy nhập key của dict cần tìm: ")
if key in my_dict:
    print(f"{key} có ở trong my_dict")
else:
    print(f"Không tìm thấy key: {key}")