from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.visited = False
        self.distance = float('inf')
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setVisited(self, visited=True):
        self.visited = visited

    def setDistance(self, dist):
        self.distance = dist

    def setPrevious(self, prev):
        self.previous = prev

    def getDistance(self):
        return self.distance

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def getVertex(self, key):
        return self.vertices.get(key)

    def addEdge(self, src, dest, weight=0):
        if src not in self.vertices:
            self.addVertex(src)
        if dest not in self.vertices:
            self.addVertex(dest)
        self.vertices[src].addNeighbor(self.vertices[dest], weight)

    def addBiEdge(self, f, t, weight=1):
        self.addEdge(f, t, weight)
        self.addEdge(t, f, weight)

    def getVertices(self):
        return self.vertices.values()

    def shortest_path(self, vertex):
        queue = deque()
        queue.append(vertex)
        vertex.setDistance(0)
        paths = [(vertex, [vertex.getId()], 0)]  # (vertex, path, cost)
        visited = {vertex}

        while queue:
            current_vertex = queue.popleft()
            current_vertex.setVisited()

            for neighbor in current_vertex.getConnections():
                if not neighbor.visited:
                    visited.add(neighbor)
                    new_distance = current_vertex.getDistance() + current_vertex.getWeight(neighbor)

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
                        paths.append((neighbor, path, neighbor.getDistance()))

        return paths
