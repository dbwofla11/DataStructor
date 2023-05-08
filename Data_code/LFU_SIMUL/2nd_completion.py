def percolateDown(x,i):
	child=2*i+1
	right=2*i+2
	if (child<=len(x)-1):
		if (right<=len(x)-1 and x[child][1]>x[right][1]):
			child = right
		if x[i][1]>x[child][1]:
			x[i],x[child]=x[child],x[i]
			percolateDown(x,child)
			
def buildHeap(x):
	for i in range((len(x) - 2) // 2, -1, -1):
		percolateDown(x,i)
	return x

def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0
    all_dict = {}
    cache={}

    data_file = open("/home/dbwofla/Desktop/DataStructor/Data_code/LFU_simulation/linkbench_short.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt+=1

        if len(all_dict)<cache_slots:
            if not lpn in all_dict:
                all_dict[lpn]=1
                cache[lpn]=1
            else:
                all_dict[lpn]+=1
                cache_hit+=1
                cache[lpn]+=1
        else:
            minheap_cache=buildHeap(list(cache.items()))
            min_frequency=minheap_cache[0][1] 
            
            if not lpn in all_dict:
                if min_frequency==1:
                    all_dict[lpn]=1
                    minheap_cache[0]=(lpn,1)
                    cache=dict(minheap_cache)
                else:
                    all_dict[lpn]=1
            else:
                if all_dict[lpn]==min_frequency and lpn in cache:
                    cache_hit+=1
                    all_dict[lpn]+=1
                    cache[lpn]+=1
                elif all_dict[lpn]==min_frequency and not lpn in cache:
                    all_dict[lpn]+=1
                    minheap_cache[0]=(lpn,all_dict[lpn])
                    cache=dict(minheap_cache)
                elif all_dict[lpn]+1<min_frequency:
                    all_dict[lpn]+=1
                elif all_dict[lpn]+1==min_frequency:
                    all_dict[lpn]+=1
                    minheap_cache[0]=(lpn,all_dict[lpn])
                    cache=dict(minheap_cache)
                else: 
                    all_dict[lpn]+=1
                    cache[lpn]+=1
                    cache_hit+=1
    return cache['0']
print(lfu_sim(100))
