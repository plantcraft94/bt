#Đỗ Thanh Tùng
# cho ví dụ list A
A = [19, 35, 0, 13, 36, 15, 13, 65, 41, 99]

for i in A:
    #tìm giá trị lớn nhất trong A
    if i == max(A):
        print(f"số lớn nhất là {i}")
        print(f"số lớn nhất ở vị trí {A.index(i)}")
    if i == min(A):
        print(f"số nhỏ nhất là {i}")
        print(f"số nhỏ nhất ở vị trí {A.index(i)}")