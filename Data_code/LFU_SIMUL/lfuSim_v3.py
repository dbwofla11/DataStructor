from LFU_heap import *

def lfu_sim(cache_size):
  cache = heap()
  PageFreq = dict()
  cache_hit = 0
  tot_cnt = 100000
  data_file = open("C:/Users/유재림/Desktop/DataStructor-master (1)/DataStructor-master/Data_code/LFU_SIMUL/linkbench.trc" , encoding="UTF-8")
  
  A = list()
  for line in data_file.readlines():
    lpn = line.split()[0]
    A.append(lpn)

  # hit 는 디셔너리 안에 있는게 빈도수가 올라갈떼 + 1
  while A:
    
    PageNum = A.pop(0)

    if cache.size() < cache_size:
      
      if PageNum in PageFreq.keys():
        PageFreq[PageNum] += 1
        cache_hit += 1
        cache.UpdateFreq(PageNum)
      else:
        PageFreq[PageNum] = 1
        cache.heapAppend([PageNum,1])

    else: # 캐시100 넘을때 하는거 
      
      if PageNum in PageFreq.keys(): # 문제 3 ) 가정 적용 시키기 
        
        if cache.IsInCache(PageNum): 
          PageFreq[PageNum] += 1
          cache_hit += 1
          cache.UpdateFreq(PageNum)
        
        else: # 예전에 들어갔다 나간 기억은 있는데 캐시에는 없는 경우 - 문제 3적용 
          PageFreq[PageNum] += 1 # 이럴때는 히트는 안올라감
          cache.UpdateMin([PageNum,PageFreq[PageNum]])

      else:
        PageFreq[PageNum] = 1
        cache.UpdateMin([PageNum,1])
        


# 문제 3 ) - 이 문제 구현 
# 나갔다 다시 들어온 것이 빈도수가 유지된다고 가정했을때 
# 캐시사이즈 3 

# (1,3) (2,3) (3,1) 

# (1,3) (2,3) (4,1) <- 4들어옴

# (1,3) (2,3) (3,2) <- 3다시 들어옴

  print("cache_slot = ", cache_size, "cache_hit = ", cache_hit, "hit ratio = ", (cache_hit / tot_cnt)*100 , "%" ) # 이 녀석이 목표임 
  print("캐시 사이즈" , cache.size())


if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)

