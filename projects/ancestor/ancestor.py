from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # Create a graph
    graph = {}
    # Keep a track of visited nodes
    visited = set()
    # Keeps a track of the path when traversing the graph
    path = []
    # add empty sets to the graph with respective indexes
    for i in ancestors:
        if i[0] not in graph:
            graph[i[0]] = set()
        if i[1] not in graph:
            graph[i[1]] = set()
    # we add the edges to the nodes
    for ancestor in ancestors:
        if ancestor[0] in graph and ancestor[1] in graph:
            graph[ancestor[1]].add(ancestor[0])
            
    # Create an empty queue
    queue = Queue()
    # Add the initial vertex to the path
    path.append(starting_node)
    # Then add the path to the queue, should be initialized as a empty list
    queue.enqueue(path)

    # This checks if the initial node has no ancestors, if it does not it returns '-1' 
    for i in graph:
        if starting_node is i and bool(graph[i]) is False:
            return -1

    # while we have something in our queue.. 
    while queue.size() > 0:
        # Dequeue the first path
        path = queue.dequeue() 
        # We grab the last vertex from the path
        last_vertex = path[-1] 
        # We check if it has NOT been visited..
        if last_vertex not in visited:
            # if not, we add it to the visited dic
            visited.add(last_vertex)
            # iterate over the last vertex's neighbors..
            for neighbor in graph[last_vertex]:
                # we check if the neighbor is NOT marked as visited...
                if neighbor not in visited:
                    # if it is not, we make a copy of the path
                    path_copy = path.copy()
                    # we append the neighbor to the copy of the path
                    path_copy.append(neighbor)
                    # then we add the copy of the path to the queue
                    queue.enqueue(path_copy)
    # we return the last vertex, indicating the farthest node in the ancestry chain
    return last_vertex

# if __name__=='__main__':
#     earliest_ancestor((1,2), 4)

