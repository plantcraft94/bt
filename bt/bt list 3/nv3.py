A=[0,4,0,1,2,3,8,9,0,1,2,3,17,-16,0,1,2]
co = False
for i in range (len(A)-2):                              #
    if A[i]==1 and A[i+1]==2 and A[i+2]==3:             #  Cre: Đình Đức
        print(f"dãy số 1,2,3 xuất hiện ở vị trí {i}")   #
        co = True
if co == False:
    print("Không tìm thấy mẫu")