DIRECTED = 'directed_graph'
UNDIRECTED = 'undirected_graph'


class GraphAdjacencyList:
    def __init__(self, typeOfGraph=UNDIRECTED):
        self.graph = {}
        self.type = typeOfGraph

    def addNode(self, value):
        if value in self.graph:
            print(f"Node with value {value} already exists")
        else:
            self.graph[value] = []

    def addEdge(self, node1, node2):

        def addEdgeInDirectedGraph(graph):
            if node1 in graph and node2 in graph:
                graph[node1].append(node2)
            else:
                print("Edge cannot be made because given node values does not exist in graph")

        def addEdgeInUnDirectedGraph(graph):
            if node1 in graph and node2 in graph:
                graph[node1].append(node2)
                graph[node2].append(node1)
            else:
                print("Edge cannot be made because given node values does not exist in graph")

        if self.type == DIRECTED:
            addEdgeInDirectedGraph(self.graph)
        elif self.type == UNDIRECTED:
            addEdgeInUnDirectedGraph(self.graph)

    def printGraph(self):
        for key, value in self.graph.items():
            print(f'{key}: ', end="")
            for node in value:
                print(f"{node},", end="")
            print()

    def createDummyGraph(self):
        graph.addNode(1)
        graph.addNode(2)
        graph.addNode(3)
        graph.addNode(4)
        graph.addEdge(1, 2)
        graph.addEdge(1, 4)
        graph.addEdge(2, 3)
        graph.addEdge(4, 3)
        graph.printGraph()


class GraphAdjacencyMatrix:
    def __init__(self):
        self.graph = []


# TODO
# 1. BFS in adjacency matrix
# 2. BFS in adjacency list
# 3. DFS in adjacency matrix
# 4. BFS in adjacency list
# 5. Connected components in graph
# 6. Detect cycle in undirected graph [BFS, DFS]
# 7. Detect cycle in directed graph [BFS, DFS]
# 8. Bipartite graph [BFS, DFS]
# 9. Topological sort DFS
# 10. Topological sort BFS (kahn's algorithm)
# 11. Smallest distance in undirected graph ?!?!
# 12. Shortest path in DAG (direct acyclic graph)
# 13. Shortest path in undirected graph (dijkstra algorithm)
# 14. Minimum spanning tree (prim's algorithm)
# 15. Disjoint set / union by rank & path compression
# 16. Kruskal's algorithm

if __name__ == '__main__':
    graph = GraphAdjacencyList(typeOfGraph=UNDIRECTED)
    graph.createDummyGraph()
