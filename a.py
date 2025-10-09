i=1
sum=0
for i in range(1,10):
    i+=1
    sum+=i
    print("sum =",sum)
    if sum % 2 == 0:
        print(f"{sum} là số chẵn")
    else:
        print(f"{sum} là số lẻ")