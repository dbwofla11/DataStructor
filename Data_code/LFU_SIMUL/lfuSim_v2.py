from LFU_heap import *

def lfu_sim(cache_size):
  cache = dict()

  cache_hit = 0
  tot_cnt = 100000
  
  data_file = open("C:/Users/유재림/Desktop/DataStructor-master (1)/DataStructor-master/Data_code/LFU_SIMUL/linkbench.trc" , encoding="UTF-8")


  A = list()
  for line in data_file.readlines():
    lpn = line.split()[0]
    A.append(lpn)

  # hit 는 디셔너리 안에 있는게 빈도수가 올라갈떼 + 1
  while A:
    
    a = A.pop(0)

    if len(cache) < cache_size:
      if a in cache:
        cache[a] += 1
        cache_hit += 1
      else:
        cache[a] = 1
    else: # 캐시100 넘을때 하는거 
      if a in cache:
        cache[a] += 1
        cache_hit += 1
      else:
        cache = list(cache.items()) # 딕셔너리 -> 이중리스트 
        cacheHeap = heap(cache) # 이중리스트 -> 힙 
        cacheHeap.buildHeap() # 힙 정렬 
        cacheHeap.deleteMin() # min (빈도수) 제거 

        cache = cacheHeap.getList() # 힙 -> 리스트 
        cache = dict(cache) # 리스트 -> 딕셔너리 

        cache[a] = 1


# 문제 3 ) - 이 문제 구현 
# 나갔다 다시 들어온 것이 빈도수가 유지된다고 가정했을때 
# 캐시사이즈 3 

# (1,3) (2,3) (3,1) 

# (1,3) (2,3) (4,1) <- 4들어옴

# (1,3) (2,3) (3,2) <- 3다시 들어옴

  print("cache_slot = ", cache_size, "cache_hit = ", cache_hit, "hit ratio = ", (cache_hit / tot_cnt)*100 , "%" ) # 이 녀석이 목표임 
  print("0 페이지 빈도수 : " , cache["0"]) 
  print("캐시 사이즈" , len(cache))


if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)

