# Python program to generate the all possible
# path of the graph from the nodes provided
graph ={
0 : [10, 15],#CARRETERA
    1 : [3, 5, 2, 6],
    2 : [1, 7, 6],
    3 : [7, 1, 8],
    4 : [1, 3, 8, 9, 5],
    5 : [1, 8, 10],
    6 : [1, 17],
    7 : [19, 11],
    8 : [11, 3, 9, 10],
    9 : [13, 11, 8, 10,4],
    10 : [0, 15, 14, 9, 5],
    11 : [12, 13, 7],
    12 : [11, 8, 13, 21],
    13 : [12, 14, 9],
    14 : [13, 10],
    15 : [0, 10, 16, 5],
    16 : [15, 17],
    17 : [6, 18],
    18 : [17],
    19 : [7],
    # 20 : [],
    21 : [12]
}

# function to generate all possible paths
def find_all_paths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
    if 'newpaths' in locals():
        for newpath in newpaths:
            paths.append(newpath)
  return paths
# Driver function call to print all
# generated paths
print(find_all_paths(graph, 0, 15))