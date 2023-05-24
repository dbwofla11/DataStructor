class heap:
    def __init__(self , list = None) -> None: 
        if list == None:
            self.node = []
        else:
            self.node = list 


    def heapAppend(self , x): # insert는 이중 리스트로 다루기 

        self.node.append(x)
        i = len(self.node) - 1 # 1
        parent = (i - 1) // 2 
        while i > 0 and self.node[i][1] > self.node[parent][1]:
            self.node[i] , self.node[parent] = self.node[parent] , self.node[i]
            i = parent
            parent = (i - 1) // 2
    

    def UpdateFreq(self , key):
        i = self.GetIndex(key)
        self.node[i][1] += 1
        self.__percolateDown(i)


    def UpdateMin(self , page): # 머리 교체 
        self.node[0] = page 
        self.__percolateDown(0)
  
    
    def GetIndex(self , key) -> int:
        for i in range(len(self.node)):
            if self.node[i][0] == key:
                FindIndex = i
                break
        return FindIndex

    # 스며오르기
    def __percolateUp(self , i:int):
        parent = (i - 1) // 2
        if i > 0 and self.node[i] > self.node[parent]:
            self.node[i] , self.node[parent] = self.node[parent] , self.node[i]
            self.__percolateUp(parent)

    # 스며내리기 
    def __percolateDown(self , i:int):
        child = 2 * i + 1
        rightChild = 2 * i + 2
        if child <= len(self.node) - 1:
            if rightChild <= len(self.node) - 1 and self.node[child][1] > self.node[rightChild][1]:
                child = rightChild
            if self.node[i][1] > self.node[child][1]:
                self.node[i] , self.node[child] = self.node[child] , self.node[i]
                self.__percolateDown(child)


    def isEmpty(self) -> bool:
        return len(self.node) == 0


    def IsInCache(self , PageNum) -> bool:
        op = False
        for i in range(len(self.node)):
            if self.node[i][0] == PageNum:
                op = True
                break
        return op
    
    def size(self) -> int :
        return len(self.node)
    

    # 아래는 안쓰는거 - (과제2에서)
    def min(self):
        return self.node[0]

    def buildHeap(self):
        for i in range( (len(self.node) - 2) // 2 , -1 , -1 ):
            self.__percolateDown(i)

    def printHeap(self):
        ncnt = 0
        for i in range( len(self.node) ):
            print(f"{self.node[i]} " , end = " ")
            if (i+2) % (2 ** ncnt) == 0:
                print()
                ncnt += 1
    
    def getList(self):
        return self.node
    

