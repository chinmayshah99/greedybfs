import warnings

class Graph(object):
    '''
        graph in the form
        {
            node = [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA = [[nodeC, weigh3]]
        }
    '''
    def __init__(self):
        self.graph = {}

    def __init__(self, graph):
        self.graph = graph
        self._node_count = 0
        self._edge_count = 0

    @property
    def node_count(self):
        return self._node_count
    
    @property
    def edge_count(self):
        return self._edge_count

    def add_node(self, node):
        '''

        '''
        if node not in self.graph:
            self.graph[node] = []
            self._node_count += 1
        else:
            raise ValueError("Node already exists in graph")

    def add_edge(self, node_start, node_end, weight):
        '''
            dsf
        '''
        
        # check if start node already exists
        if node_start not in self.graph:
            warnings.warn('The start node does not exist, adding it to graph', Warning)
            self.add_node(node_start)
            edges = self.graph[node_start]
        
        #check if edge already exists
        for item in edges:
            if item[0] == node_end:
                raise ValueError("Edge already exiists")

        # check if end node already exists
        if node_end not in self.graph:
            warnings.warn('The end node does not exist, adding it to graph', Warning)
            self.add_node(node_end)

        self.graph[node_start].append([node_end, weight])
        self._edge_count += 1

    def delete_node(self, node):
        '''
            Removoes all graph dependecnies and then removes node
            #TODO
        '''
        self.graph.pop(node, None)
        self._edge_count -=1

    def delete_edge(self, node_start, node_end):
        edges = self.graph[node_start]
        for item in edges:
            if item[0] == node_end:
                self.graph[node_start].remove(item)

        self._edge_count -=1
        
    def get_node_details(self, node):
        if node in self.graph:
            return self.graph[node]
