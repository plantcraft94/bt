import random as rd
print("Đỗ Thanh Tùng - 11A4")

n = int(input("Nhập số lượng phần tử của dãy số, N = "))
a = []
for i in range(n):
    ai = rd.randint(-300, 300)
    a += [ai]
print("Mảng vừa tạo:")
print(a)
i = n
while (i > 1):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            tam = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tam
    i -= 1
print("Dã số đã được sắp xếp:")
print(a)
input()
