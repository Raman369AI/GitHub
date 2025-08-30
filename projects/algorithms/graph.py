'''Code for understanding queue and graph algorithms'''
# Nodes and Edges are the primary matter of concern.
# Nodes are also called as vertices.
# edge is a connection between the nodes, information stored in it is called as weight.



class queue:
    def __init__(self):
        self.data = []
        self.index = 0
    def enqueue(self,num):
        self.data.append(num)
    def dequeue(self):
        if len(self.data) == 0:
            print('queue is empty')
        else:
            self.data.pop(0)
    def print_queue(self):
        print(self.data)
    def first(self):
        if len(self.data) > 0:
            print(self.data[0])
        else:
            print('queue is empty')
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def len(self):
        print(len(self.data))
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
# Determine the nodes to which 1 node is conencted.
'''Adjacency list: Contains a list for each node with list of all nodes that are neighbours.'''
class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes
        self.nodes = queue()
        #[[]]*num_nodes never works as it creates the same element, all elemets are updated in unison.
        self.data = [[] for _ in range(num_nodes)]
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.visited = [[False] * num_nodes for _ in range(num_nodes)]
        for x,y in edges:
            #insert edges into right adjacent list
            self.data[x].append(y)
            self.data[y].append(x)
            self.adj_matrix[x][y] = 1
        
    ''' Building adjacency matrix and list'''
    #def adjacency(self, num_nodes):
    #def BFS(self):

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def print_adj_list(self):
        for row in self.data:
            print(row)
    
    def get_edge(self,u,v):
        if v in self.data[u]:
            print('Conencted nodes')
        else:
            print('No connection')
    
    def vertex_count(self):
        print(f'The no of vertexes are {len(self.adj_matrix)}')
    ## Queue Data Strucutre will be used FIFO.
    # Travel the vertices that are close to root vertices.

    '''We choose a random node as level 0, append all the adjecent nodes '''
    def reachable(self,u):
        self.nodes.enqueue(u)
        self.visited[u] = True
        #print(self.adj_matrix[u])
        #for i in self.data[u]:
            
               

    def print_nodes(self):
        self.nodes.print_queue()

                    
    
    #def edge_nodes(self,u,v):





    #def graph_traversal(self):
        #self.data
#graph1.print_adj_list()
#graph1.get_edge(3,9)
#graph1.vertex_count()
graph1 = Graph(num_nodes,edges)

#graph1.reachable(3)
graph1.print_nodes()


#q.print_queue()

