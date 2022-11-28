A = [4,5,6,1,2,3,7,8,9,10]

#quan trọng (nếu nó đúng :) )
for i in A:
    if i == 1:
        a = A.index(i)
        if A[a] == 1 and A[a+1] == 2 and A[a+2] == 3:
            print(f"vị trí bắt đầu của dãy số 1,2,3 là {a}")
            break
        else:
            print("Không tìm thấy mẫu")
            break

    elif i == A[-1]:
        print("Không tìm thấy mẫu")
#chắc đúng đấy :) bài khó vl