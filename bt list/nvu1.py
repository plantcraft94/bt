#Đỗ Thanh Tùng
n = int(input("Nhập số phần tử của list: "))
A = []
for i in range(n):
    ten = input("Nhập tên: ")
    A.append(ten)

print("Danh sách tên vừa nhập là: ")
for m in A:
    print(m)
