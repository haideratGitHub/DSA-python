class Graph:
    def __init__(self, type='list', numberOfNodes=1):
        if type == 'matrix':
            self.graph = [[0] * numberOfNodes] * numberOfNodes
        elif type == 'list':
            self.graph = {}
            for i in range(numberOfNodes):
                self.graph[i] = []


if __name__ == '__main__':
    graph = Graph('list', 2)
