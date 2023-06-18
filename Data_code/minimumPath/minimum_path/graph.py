import heapq

class WeightGraph():
    def __init__(self) -> None:
        self.graph = dict()

    def addEdge(self , start , end , weight):
        if start not in self.graph:
            self.graph[start] = dict()
        self.graph[start][end] = weight
        