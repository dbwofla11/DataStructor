def quickSort(A , L:int , R:int):
    if L < R:
        q = partition(A , L , R)
        quickSort(A , L , q-1)
        quickSort(A , q+1 , R)
    

def partition(A , L:int , R:int) -> int:
    x = A[R][1] # 빈도수 
    i = L-1
    for k in range(L , R):
        if A[k][1] < x: # 빈도수 비교
            i += 1
            A[i],A[k] = A[k] , A[i]
    A[i+1] , A[R] = A[R] , A[i+1]
    return i+1


def quickSort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][1] # 첫번째 열을 pivot으로 선택
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i][1] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quickSort2(left) + [arr[0]] + quickSort2(right)

# quickSort set 테스트 
# arr = [('31122',1), ('21241',5) , ('1123',8) , ('412323',2) , ('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2)]
# sorted_arr = quickSort2(arr)
# print(sorted_arr)