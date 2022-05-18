# from collections import defaultdict

# graph = defaultdict(list)

# def addEdge(graph,u,v):
#     graph[u].append(v)
 
# # definition of function

class ciudadGT:
    def __init__(self, zonas):
        self.zonas = zonas
    
    def generate_edges(self):
        edges = []
    # for each node in graph
        for node in self.zonas:
        # for each neighbour node of a single node
            for neighbour in self.zonas[node]:
            # if edge exists then append
                edges.append((node, neighbour))
        return edges
        
    def find_all_paths(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.zonas[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
            if 'newpaths' in locals():
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in self.zonas[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
