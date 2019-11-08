from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices:
            self.vertices[v1] = v2

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # initialise a queue data structure and append starting_vertex as the first item in a list
        q = Queue()
        q.enqueue([starting_vertex])
        # initialise an empty set of visited vertices
        visited_vs = set()
        # while the queue is not empty, keep traversing
        while q.size():
            # dequeue the next path and store it in a variable
            p = q.dequeue()
            # grab the last vertex from the path
            v = p[len(p) - 1]
            # if the vertex has not already been visited
            if v not in visited_vs:
                # look for a ? in the list of dirs
                for dir in self.vertices[v]:
                    if self.vertices[v][dir] == '?':
                        return p
                # if you find a ? then return p

                # add the vertex to the visited set
                visited_vs.add(v)
                # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
                for next_vertex in self.vertices[v]:
                    # make a copy of the current path
                    p_copy = p[:]
                    # append the next_vertex to the path and enqueue
                    p_copy.append(self.vertices[v][next_vertex])
                    q.enqueue(p_copy)
        # return False if the destination_vertex is not in  the graph
        return False
