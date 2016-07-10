import pprint
from collections import deque

def myBFS(root, goal):
    Q = deque([[root]])
    count = 0
    All_Paths = []

    while Q:
        curr_path = Q.pop()
        node = curr_path[-1]

        if node == goal:

            All_Paths.append(curr_path)
            count += 1
            #print curr_path, count

        for adj in graph.get(node, []):
            if adj not in curr_path:
                new_path = curr_path[:]
                new_path.append(adj)
                #print new_path
                Q.append(new_path)
    return All_Paths, count


graph = {}

s = 3
for y in range(s):
    for x in range(s):

        graph.setdefault((y,x),[])
        try:
            graph[(y,x)].append((y+1,x))
        except IndexError:
            pass
        try:
            graph[(y,x)].append((y,x+1))
        except IndexError:
            pass


#graph.pop((20,20))

graph = {k:[p for p in v if 21 not in p] for k,v in graph.items()}

pprint.pprint(graph)

foo = myBFS(root=(0,0), goal=(2,2))
print foo[0]

"""
for path in foo[0]:
    print path
"""
print "Count of", s, "sides", foo[1]
