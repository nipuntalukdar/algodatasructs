import unittest

class graph(object):
    def __init__(self):
        self.vertices = {}

    def add_node(self, node):
        if node not in self.vertices:
            self.vertices[node] = set()

    def add_edge(self, node1, node2):
        if node1 not in self.vertices or node2 not in self.vertices:
            return
        self.vertices[node1].add(node2)
        self.vertices[node2].add(node1)

    def bfs(self):
        if not self.vertices:
            return
        ks = set(self.vertices.keys())
        start = ks.pop()
        visited = []
        q = [start]
        while True:
            if not q:
                if not ks:
                    return visited
                q.append(ks.pop())
                continue
            start = q.pop(0)
            if start in visited:
                continue
            visited.append(start)
            for connct in self.vertices[start]:
                if connct in visited:
                    continue
                q.append(connct)

    def dfs(self):
        if not self.vertices:
            return
        ks = set(self.vertices.keys())
        start = ks.pop()
        visited = []
        q = [start]
        while True:
            if not q:
                if not ks:
                    return visited
                q.append(ks.pop())
                continue
            # For dfs we pull the last element pushed to stack
            start = q.pop()
            if start in visited:
                continue
            visited.append(start)
            for connct in self.vertices[start]:
                if connct in visited:
                    continue
                q.append(connct)

    def detect_cycle(self):
        ''' returns true if a cycle is detected in the graph'''
        if not self.vertices:
            return False
        ks = self.vertices.keys()
        cur_visited = set()
        start = None
        q = []
        while True:
            if not q:
                if not ks:
                    return False
                start = ks.pop()
                cur_visited.clear()        
                q = []
                camefrom = None
            else:
                start, camefrom = q.pop(0) 
            cur_visited.add(start)
            for i in self.vertices[start]:
                # if the node is pointing to last node in the path "camefrom", then 
                # ignore
                if i == camefrom:
                    continue
                if i in cur_visited:
                    return True
                # append in the stack the node i and camefrom which is start
                q.append((i, start))
                if i in ks:
                    ks.remove(i)

        return False

    def color(self):
        taken_colors = set()
        if not self.vertices:
            return taken_colors
        color_vertex = {}
        neighbour_color = set()

        for k in self.vertices:
            if k in color_vertex: continue
            for neighbour in self.vertices[k]:
                nc = color_vertex.get(neighbour, None)
                if nc is not None:
                    neighbour_color.add(nc)
            remaining_color = taken_colors - neighbour_color
            if not remaining_color:
                # a new colour is needed
                new_color = len(taken_colors)
                taken_colors.add(new_color)
                color_vertex[k] = new_color
            else:
                # take the lowest color of colors already taken and which is not
                # taken by its neighbours
                color_vertex[k] = remaining_color.pop()
            neighbour_color.clear()
        return taken_colors
            
    
class TestBfs(unittest.TestCase):
    def setUp(self):
        self.graph = graph()
    
    def tearDown(self):
        self.graph = graph()

    def test_bfs(self):
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1,2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_node(100)
        self.graph.add_node(5)
        self.graph.add_edge(2,3)
        self.graph.add_edge(3,4)
        self.graph.add_edge(4,100)
        self.graph.add_edge(100,5)
        nodes = self.graph.bfs()
        print ', '.join([str(a) for a in nodes])
        nodes = self.graph.dfs()
        print ', '.join([str(a) for a in nodes])


class TestCycle(unittest.TestCase):
    def setUp(self):
        self.graph = graph()
    
    def tearDown(self):
        self.graph = graph()

    def test_cycle(self):
        gr = self.graph
        gr.add_node(1)
        gr.add_node(2)
        gr.add_edge(1,2)
        gr.add_node(3)
        gr.add_node(4)
        gr.add_edge(2,3)
        gr.add_edge(3,4)
        gr.add_node(5)
        gr.add_edge(4,2)
        self.assertTrue(self.graph.detect_cycle())

    def test_colors(self):
        gr = self.graph
        gr.add_node(1)
        gr.add_node(2)
        self.assertEqual(1, len(gr.color()))
        gr.add_edge(1,2)
        self.assertEqual(2, len(gr.color()))
        gr.add_node(3)
        self.assertEqual(2, len(gr.color()))
        gr.add_edge(2,3)
        self.assertEqual(2, len(gr.color()))
        gr.add_edge(3,1)
        self.assertEqual(3, len(gr.color()))
        gr.add_edge(4,2)
        gr.add_edge(4,3)
        self.assertEqual(3, len(gr.color()))

if __name__ == '__main__':
   unittest.main()
