#VD
A = [1,2,2,3,4,5,5,6,7,8,9,10]

# chỗ quan trọng bắt đầu từ đây
if len(A)%2 != 0:
    del A[len(A)//2]
    print(A)

elif len(A)%2 == 0:
    del A[len(A)//2]
    del A[len(A)//2]
    print(A)
