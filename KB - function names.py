import graphs
from graphs import Graph, Vertex

def bacon_degree(g, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""
    start_vertex = g.getVertex(actor)
    shortest_degree = g.shortest_path(start_vertex)

    bacon_number = float('inf')
    for vertex, _, distance in shortest_degree:
        if vertex.getId().lower() == 'kevin bacon':
            bacon_number = min(bacon_number, distance)

    return bacon_number




def actors_with_bacon_degree(g, bacon_number):
    """Returns a list of actors with a given Bacon number"""
    actors = []
    for vertex in g.getVertices():
        if bacon_degree(g, vertex.getId()) == bacon_number and vertex.getId() != 'Kevin Bacon':
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

print(bacon_degree(g, 'Tom Hanks'))
print(bacon_degree(g, 'Tom Hanks'))
print(actors_with_bacon_degree(g, 2))
print(highest_bacon(g))