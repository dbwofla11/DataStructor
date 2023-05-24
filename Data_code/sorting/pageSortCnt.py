from Quick_sort import *
from mergesort import *


import sys
limit_number = 1500000
sys.setrecursionlimit(limit_number)


def page_sort(input_file):
    
    dataFile = open(input_file)
    A = []
    for line in dataFile.readlines():
        L = line.split()[0]
        A.append(L)
    
    # 카운트 세기 
    count = dict()
    for k in A:
        if k in count:
            count[k] += 1 
        else:
            count[k] = 1

    cnt_list = list(count.items())

    # 초기 파일 주소 10개 ( 처음 ~ 10 )
    for i in range(10):
        print(cnt_list[i] , end = ' ')
    print("")

    sorted_arr_quick = quickSort2(cnt_list)
    # sorted_arr_merge = mergeSort2(cnt_list)

    # 카운트 출력 
    print("\n퀵 정렬 ( 빈도수 )")
    for i in range(10):
        print(sorted_arr_quick[i] , end=" ")
    print("")

    # print("\n병합 정렬 ( 빈도수 )")
    # for i in range(10):
    #     print(sorted_arr_merge[i] , end=" ")
    # print("")

if __name__ == "__main__":
    page_sort("/home/dbwofla/Desktop/DataStructor/Data_code/sorting/linkbench_short.trc")