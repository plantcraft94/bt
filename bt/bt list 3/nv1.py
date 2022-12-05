A = []
n = int(input("Nhập n: "))
for a in range(n):
    ten = input("Nhập tên: ")
    A.insert(0,ten)

print("Tên mỗi học sinh là: ")
for i in A:
    print(i)