# -*- coding: utf-8 -*-

from priorityQueue import PriorityQueue
from graph import Graph

#     test_graph = {
#         "a": [['s',253], ['t', 329], ['z',374]],
#         "s": [['f', 176], ['o', 380], ['r', 193]],
#         "f": [['b', 0]]
#     }


def gbfs(start_node, end_node, graph_input={}):
    path = []
    myQueue = PriorityQueue()
    graph = Graph(graph_input)

    start_node = start_node
    end_node = end_node

    print(start_node, end='')
    start = graph.get_node_details(start_node)
    current_node = [start_node]

    while current_node[0] != end_node:
        current_node = graph.get_node_details(current_node[0])
        myQueue.makeEmpty()

        for item in current_node:
            myQueue.insert(item)

        current_node = myQueue.delete()
        path.append(current_node[0])
        # print("-> " + str(current_node[0]) , end = '')
    return path
