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
      cache = list(cache.items()) # 딕셔너리 -> 리스트 
      cacheHeap = heap(cache) # 
      cacheHeap.buildHeap()
      cacheHeap.deleteMax()

      cache = cacheHeap.getList()
      cache = dict(cache)


  print(cache) 
  print("cache_slot = ", cache_size, "cache_hit = ", cache_hit, "hit ratio = ", (cache_hit / tot_cnt)*100 , "%" ) # 이 녀석이 목표임 
  print("0 페이지 빈도수 : " , cache["0"]) 


if __name__ == "__main__":
  # for cache_slots in range(100, 1001, 100):
  lfu_sim(100)


# 캐시 사이즈 3 
# 1 1 1

# 1 2 1 

# 1 2 2 

# 3 2 2 

# 3 2 1  x 

# 3 2 2  o


# 캐시사이즈 3 

# (1,3) (2,3) (3,1) 

# (1,3) (2,3) (4,1) <- 4들어옴

# (1,3) (2,3) (3,2) <- 3다시 들어옴

