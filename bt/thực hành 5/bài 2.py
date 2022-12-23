print("Đỗ Thanh Tùng - 11A4")

a = input("nhập xâu: ")
for i in a:
    count = 0
    for j in a:
        if i.lower() == j.lower():
            count += 1
    print(f"chữ {i} xuất hiện {count} lần")