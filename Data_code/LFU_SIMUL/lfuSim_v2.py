from LFU_heap import *

def lfu_sim(cache_size):
  cache = dict()

  cache_hit = 0
  tot_cnt = 10000
  
  data_file = open("/home/dbwofla/Desktop/DataStructor/Data_code/LFU_simulation/linkbench_short.trc")


  A = list()
  for line in data_file.readlines():
    lpn = line.split()[0]
    A.append(lpn)

  # hit 는 디셔너리 안에 있는게 빈도수가 올라갈떼 + 1
  while A:
    
    a = A.pop(0)

    if len(cache) <= cache_size:
      if a in cache:
        cache[a] += 1
        cache_hit += 1
      else:
        cache[a] = 1
    else:
      cache = list(cache.items()) # 딕셔너리 -> 이중리스트 
      cacheHeap = heap(cache) # 이중리스트 -> 힙 
      cacheHeap.buildHeap() # 힙 정렬 
      cacheHeap.deleteMax() # min (빈도수) 제거 

      cache = cacheHeap.getList() # 힙 -> 리스트 
      cache = dict(cache) # 리스트 -> 딕셔너리 

# 문제 1 : 1로 초기화 되는거 
# 문제 2 : 캐시사이즈 넘을 때 추가 안되는거 

    
  print(cache) 
  print("cache_slot = ", cache_size, "cache_hit = ", cache_hit, "hit ratio = ", (cache_hit / tot_cnt)*100 , "%" ) # 이 녀석이 목표임 
  print("0 페이지 빈도수 : " , cache["0"]) 


if __name__ == "__main__":
  # for cache_slots in range(100, 1001, 100):
  lfu_sim(100)


# 나갔다 다시 들어온 것이 빈도수가 유지된다고 가정했을때 

