#Đỗ Thanh Tùng
n = int(input("Nhập số phần tử của list: "))
A = []
for i in range(n):
    so = int(input("Nhập số: "))
    A.append(so)

tong = sum(A)
tbc = tong/n

print(f"Tổng các số trong list là: {tong}, trung bình cộng là: {tbc}")
print(A)
