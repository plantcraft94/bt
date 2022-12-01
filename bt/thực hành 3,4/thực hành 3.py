import random as rd
print("Đỗ Thanh Tùng - 11A4")

n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = rd.randint(-300, 300)
    a.append(x)
    
print(a)
k = int(input("Nhập số nguyên k: "))
s = 0
for i in a:
    if i%k == 0:
        s += i

print(f"Tổng cần tính là: {s}")