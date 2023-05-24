def mergeSort(A , L:int , R:int):
    if L < R:
        middle = (L + R) // 2
        mergeSort(A , L , middle)
        mergeSort(A , middle , R)
        merge(A , L , middle , R)
    

def merge(A , L:int , middle:int , R:int):
    i = L; k = middle + 1 ; t = 0 
    temp = [0 for i in range(len(A))]
    while i <= middle and k <= R:
        if A[i] <= A[k]:
            temp[t] = A[i]; t += 1; i += 1
        else:
            temp[t] = A[k]; t += 1; k += 1

    while i <= middle:
        temp[t] = A[i]; t += 1; i += 1

    while k <= R:
        temp[t] = A[k]; t += 1; k += 1
    
    i = L; t = 0
    while i <= R:
        A[i] = temp[t]; t += 1; i += 1


def mergeSort2(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left_arr = mergeSort2(arr[:middle])
        right_arr = mergeSort2(arr[middle:])

        mergeed_arr = []
        left_i = right_i = 0
        while left_i < len(left_arr) and right_i < len(right_arr):
            if left_arr[left_i][1] > right_arr[right_i][1]:
                mergeed_arr.append(left_arr[left_i])
                left_i += 1
            else:
                mergeed_arr.append(right_arr[right_i])
                right_i += 1
        
        mergeed_arr += left_arr[left_i:]
        mergeed_arr += right_arr[right_i:]

        return mergeed_arr

# 머지 소트 테스트 
mergeTest = [('31122',1), ('21241',5) , ('1123',8) , ('412323',2) , ('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2),('41232123',2)]
marr = mergeSort2(mergeTest)
print(marr)