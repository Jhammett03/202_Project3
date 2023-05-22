import graphs
from collections import deque
from graphs import Graph, Vertex

def bacon_degree(g, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""
    graph_copy = Graph()  # Create a new graph object
    vertex_mapping = {}  # Mapping of original vertices to copied vertices

    # Create copied vertices and add them to the copied graph
    for original_vertex in g.getVertices():
        copied_vertex = graph_copy.addVertex(original_vertex.getId())
        vertex_mapping[original_vertex] = copied_vertex

    # Add copied edges to the copied graph
    for original_vertex in g.getVertices():
        copied_vertex = vertex_mapping[original_vertex]
        for original_neighbor in original_vertex.getConnections():
            copied_neighbor = vertex_mapping[original_neighbor]
            weight = original_vertex.getWeight(original_neighbor)
            graph_copy.addEdge(copied_vertex.getId(), copied_neighbor.getId(), weight)

    start_vertex = graph_copy.getVertex('Kevin Bacon')  # Set Kevin Bacon as the starting vertex
    if start_vertex is None:
        return -1  # Kevin Bacon not found in the graph

    queue = deque()
    queue.append(start_vertex)
    start_vertex.setDistance(0)
    paths = [(start_vertex, [], 0)]  # (vertex, path, cost)
    visited = {start_vertex}

    while queue:
        current_vertex = queue.popleft()
        current_vertex.setVisited()

        for neighbor in current_vertex.getConnections():
            if neighbor not in visited:
                visited.add(neighbor)
                new_distance = current_vertex.distance + current_vertex.getWeight(neighbor)
                if new_distance < neighbor.distance:
                    neighbor.setDistance(new_distance)
                    neighbor.setPrevious(current_vertex)
                    queue.append(neighbor)

                    # Update paths
                    path = [neighbor.getId()]  # Start path with the current neighbor
                    v = neighbor
                    while v.previous is not None:
                        path.insert(0, v.previous.getId())  # Store vertices instead of edges
                        v = v.previous
                    paths.append((neighbor, path, new_distance))

    bacon_number = -2
    for vertex, _, _ in paths:
        if vertex.getId() == actor:
            bacon_number = vertex.getDistance()
            break

    return bacon_number


def actors_with_bacon_degree(g, bacon_number):
    """Returns a list of actors with a given Bacon number"""
    actors = []
    for vertex in g.getVertices():
        if bacon_degree(g, vertex.getId()) == bacon_number:
            actors.append(vertex.getId())
    return actors


def highest_bacon(g):
    """Returns the actor(s) with the highest Bacon degree"""
    max_bacon_degree = -1
    bacon_actors = []

    for vertex in g.getVertices():
        bacon_number = bacon_degree(g, vertex.getId())
        if bacon_number > max_bacon_degree:
            max_bacon_degree = bacon_number
            bacon_actors = [vertex.getId()]
        elif bacon_number == max_bacon_degree:
            bacon_actors.append(vertex.getId())

    return bacon_actors


def any_actors_degree(g, actor1, actor2):
    """A more general function to return the path length between any two actors"""
    start_vertex = g.getVertex(actor1)
    if start_vertex is None:
        return -1  # Actor1 not found in the graph

    queue = deque()
    queue.append(start_vertex)
    start_vertex.setDistance(0)
    visited = {start_vertex}

    while queue:
        current_vertex = queue.popleft()
        current_vertex.setVisited()

        if current_vertex.getId() == actor2:
            return current_vertex.getDistance()

        for neighbor in current_vertex.getConnections():
            if neighbor not in visited:
                visited.add(neighbor)
                new_distance = current_vertex.getDistance() + current_vertex.getWeight(neighbor)
                neighbor.setDistance(new_distance)
                queue.append(neighbor)

    return -1  # Actor2 not found or there is no path between actor1 and actor2



    # Code to build the example graph:
    # Note that the addBiEdge function adds two edges to account for undirected edges.
    # add this function to your graph class:

def addBiEdge(self, f, t, weight=1):
    self.addEdge(f, t, weight)
    self.addEdge(t, f, weight)

g = graphs.Graph()
g.addVertex('Kevin Bacon')
g.addVertex('Tom Hanks')
g.addVertex('Bill Paxton')
g.addVertex('Paul Herbert')
g.addVertex('Yves Aubert')
g.addVertex('Shane Zaza')
g.addVertex('Seretta Wilson')
g.addVertex('Meryl Streep')
g.addVertex('John Beluci')
g.addVertex('Kathleen Quinlan')
g.addVertex('Donald Sutherland')
g.addVertex('Lloyd Bridges')
g.addVertex('Grace Kelly')
g.addVertex('Nicole Kidman')
g.addVertex('Patrick Allen')
g.addVertex('Glenn Close')
g.addVertex('John Gielgud')
g.addVertex('Vernon Dobtcheff')
g.addVertex('Kate Winslet')

g.addBiEdge('Kevin Bacon', 'Tom Hanks')
g.addBiEdge('Kevin Bacon', 'John Beluci')
g.addBiEdge('Kevin Bacon', 'Meryl Streep')
g.addBiEdge('Kevin Bacon', 'Donald Sutherland')
g.addBiEdge('Kevin Bacon', 'Bill Paxton')
g.addBiEdge('Kevin Bacon', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Bill Paxton')
g.addBiEdge('Tom Hanks', 'Paul Herbert')
g.addBiEdge('Tom Hanks', 'Yves Aubert')
g.addBiEdge('Tom Hanks', 'Shane Zaza')
g.addBiEdge('Tom Hanks', 'Seretta Wilson')
g.addBiEdge('Tom Hanks', 'Lloyd Bridges')
g.addBiEdge('Lloyd Bridges', 'Grace Kelly')
g.addBiEdge('Donald Sutherland', 'Patrick Allen')
g.addBiEdge('Donald Sutherland', 'Nicole Kidman')
g.addBiEdge('Donald Sutherland', 'Vernon Dobtcheff')
g.addBiEdge('Nicole Kidman', 'Glenn Close')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Bill Paxton', 'Kate Winslet')
g.addBiEdge('Patrick Allen', 'John Gielgud')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Vernon Dobtcheff', 'John Gielgud')


print(bacon_degree(g, 'Nicole Kidman'))
print(actors_with_bacon_degree(g, 2))
print(highest_bacon(g))
print(any_actors_degree(g, 'Kevin Bacon', 'Kate Winslet'))
print(any_actors_degree(g, 'Kate Winslet', 'John Gielgud'))