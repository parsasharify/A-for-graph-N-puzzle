import heapq

input_ = input().split()
n = int(input_[0])

m = int(input_[1])

graph = [ [] for i in range(n) ]
#print(graph)

for i in range(m):
    input_ = input().split()
    v1 = int(input_[0])
    v2 = int(input_[1])
    graph[v1].append(v2)
    graph[v2].append(v1)


labels = []
dest_label = []
input_ = input().split()
for i in range(n):
    labels.append(int(input_[i]))
    dest_label.append(i)

rows, cols = (n, n)
arr = [[0 for i in range(cols)] for j in range(rows)]
#print(arr)











def BFS(adj, src, v, dist):

    queue = []

    visited = [False for i in range(v)]


    for i in range(v):
        dist[i] = 1000000
        #pred[i] = -1


    visited[src] = True
    dist[src] = 0
    queue.append(src)
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):

            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                #pred[adj[u][i]] = u
                queue.append(adj[u][i])


for start in range(n):


  #  pred = [0 for i in range(n)]
    dist = [0 for i in range(n)]
    BFS(graph, start, n, dist)
    arr[start] = dist

#print(arr)

class state:
    def __init__(self, labels, zero_label_index):
        self.label_state = labels
        self.f_value = 1000000
        self.zero_label_index = zero_label_index

    def __lt__(self, other):
        return self.f_value < other.f_value
    def get_label_state(self):
        return self.label_state
    def get_f_value(self):
        return self.f_value
    def se_f_value(self, value):
        self.f_value = value


class Graph:

    def __init__(self, graph , arr):
        self.graph = graph
        self.arr = arr


    def get_neighbor_state(self, v, zero_label_index):

        #zero_label_index = -1
        #for i in range(len(v)):
        #    if v[i] == 0:
        #        zero_label_index = i
        #        break

        return_list = []
        return_list_zero_index = []

        for swap_index in self.graph[zero_label_index]:
            adding_state = v.copy()
            adding_state[zero_label_index] = v[swap_index]
            adding_state[swap_index] = 0
            return_list.append(adding_state)
            return_list_zero_index.append(swap_index)

        return tuple([return_list, return_list_zero_index])

    def h(self, n):

        h_value = 0

        for i in range(len(n)):
            if(n[i] != 0):
                h_value += self.arr[i][n[i]]

        return h_value

    def a_star_algorithm(self, start_node, stop_node):


        open_list = []
        open_list_labels = []
        open_list_labels.append(start_node)
        for i in range(len(start_node)):
            if start_node[i] == 0:
                adding_state = state(start_node, i)
                break

        adding_state.se_f_value(0+self.h(start_node))
        heapq.heapify(open_list)
        heapq.heappush(open_list, adding_state)
        closed_list =  set()

        g = {}

        g[tuple(start_node)] = 0


        while len(open_list) > 0:

            if(len(open_list) != 0):
                hold_state = heapq.heappop(open_list)
                n = hold_state.get_label_state()
                zero_label_index = hold_state.zero_label_index
            else:
                print('Path does not exist!')
                return None

            if n == stop_node:

                return g[tuple(n)]

            hold_neighbors = self.get_neighbor_state(n, zero_label_index)
            for p in range(len(hold_neighbors[0])):#self.get_neighbor_state(n, zero_label_index)
#                m not in open_list_labels and
                m = hold_neighbors[0][p]
                if  tuple(m) not in closed_list:
                    new_state = state(m, hold_neighbors[1][p])
                    hold = g[tuple(n)] + 1
                    g[tuple(m)] = hold
                    new_state.se_f_value(hold + self.h(m))
                    open_list_labels.append(m)
                    heapq.heappush(open_list, new_state)

                else:
                    if g[tuple(m)] > g[tuple(n)] + 1:
                        hold_2 = g[tuple(n)] + 1
                        g[tuple(m)] = hold_2

                        if tuple(m) in closed_list:
                            closed_list.remove(tuple(m))
                        new_state = state(m, hold_neighbors[1][p])
                        new_state.se_f_value(hold_2 + self.h(m))
                        open_list_labels.append(m)
                        heapq.heappush(open_list, new_state)



            open_list_labels.remove(n)
            closed_list.add(tuple(n))

        print('Path does not exist!')
        return None

graph1 = Graph(graph=graph , arr=arr)
print(graph1.a_star_algorithm( labels, dest_label))

#4 5
#1 3
#2 0
#2 1
#1 0
#3 0
#0 3 1 2