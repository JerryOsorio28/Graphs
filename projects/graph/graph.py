"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Hint: https://docs.python-guide.org/writing/gotchas/

        if visited is None:
            visited = set()

        # we check if the vertex (node) is in visited
        if starting_vertex not in visited:
            # if it is not,3 we added to the set
            visited.add(starting_vertex)
        # After adding it to the visited set (or not), we print the node
        print('starting_vertex', starting_vertex)
        # Then we iterate over the neighbors of the node
        for neighbor in self.get_neighbors(starting_vertex):
            # we check if the neighbors are in the visited set...
            if neighbor not in visited:
                # if they are NOT, we call the function recursively on it.
                self.dft_recursive(neighbor, visited=visited)

# {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}


    def bfs(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        queue = Queue()
        # Add the initial vertex to the path
        path.append(starting_vertex)
        # Then add the path to the queue, should be initialized as a empty list
        queue.enqueue(path)
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue, the first PATH
            path = queue.dequeue() 
            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1] 
            # CHECK IF IT'S THE TARGET
            if last_vertex is destination_vertex:
                # IF SO, RETURN THE PATH
                print('right path', path)
                return path
            # else check if it's been visited
            if last_vertex not in visited:
            # If it has not been visited...
                # Added to the visited dic
                visited.add(last_vertex)
                # iterate over the last vertex's neighbors..
                for neighbor in self.get_neighbors(last_vertex):
                    # we check if the neighbor is NOT marked as visited...
                    if neighbor not in visited:
                        # if it is not, we make a copy of the path
                        path_copy = path.copy()
                        # we append the neighbor to the copy of the path
                        path_copy.append(neighbor)
                        # then we add the copy of the path to the queue
                        queue.enqueue(path_copy)
        print('Vertex not found')

    def dfs(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # we initialize our path to an empty list and visited to an empty set
        # we create our Stack
        stack = Stack()
        # we need to add the starting vertex to our path
        path.append(starting_vertex)
        # then we add our path to our stack
        stack.push(path)
        # and while our stack is not empty...
        while stack.size() > 0:
            # we want to pop the first path
            path = stack.pop()
            # we want to grab the last value of the path
            last_vertex = path[-1]
            # and we check if the last value is the target
            if last_vertex is destination_vertex:
                # if it is we return it
                print('right path', path)
                return path
            # we also want to check if it is marked as visited..
            if last_vertex not in visited:
                #  if it's not already we mark it
                visited.add(last_vertex)
            # if it is not our target, we want to get the neighbors
            for neighbor in self.get_neighbors(last_vertex):
                # we make a copy of the path
                path_copy = path.copy()
                # we add the neighbor to the copy of the path
                path_copy.append(neighbor)
                # and we push the copy of the path to the Stack
                stack.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if path is None:
            path = []

        if starting_vertex not in path:
            # we append our starting vertex to the path
            path.append(starting_vertex)
        # we grab the last value in our path
        last_vertex = path[-1]
        if last_vertex is destination_vertex:
            print('right path', path)
            return path
        # we check if the vertex (node) is in visited
        if last_vertex not in visited:
            # if it is not,3 we added to the set
            visited.add(last_vertex)
        # Then we iterate over the neighbors of the node
        for neighbor in self.get_neighbors(last_vertex):
            # we check if the neighbors are in the visited set...
            if neighbor not in visited:
                # if they are NOT, we call the function recursively on it.
                self.dfs_recursive(neighbor, destination_vertex, path=path, visited=visited)
            if neighbor in path:
                path.pop()
            
        # path = [1,2,3,5]
        # visitied = {1,2,3,5,}

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5 
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)
    # print('--------------')
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # graph.bfs(1, 6)

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # graph.dfs(1, 6)
    # graph.dfs_recursive(1, 6)