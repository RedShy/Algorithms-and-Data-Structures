# grafo con liste di adiacenze


class QueueItem:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def enqueue(self, value) -> None:
        item = QueueItem(value=value, next=self.start, previous=None)
        if self.start:
            self.start.previous = item

        self.start = item

        if not self.end:
            self.end = self.start

    def dequeue(self) -> any:
        if not self.end:
            raise Exception("Empty List")

        value = self.end.value
        self.end = self.end.previous

        if self.end:
            self.end.next = None

        return value

    def __next__(self):
        try:
            return self.dequeue()
        except:
            raise StopIteration

    def __iter__(self):
        return self


class Node:
    def __init__(self, value=None) -> None:
        self.adjacent_nodes = set()
        self.value = value

    def add_adjacent(self, node) -> None:
        self.adjacent_nodes.add(node)

    def add_adjacents(self, *nodes) -> None:
        for node in nodes:
            self.add_adjacent(node)

    def __repr__(self) -> str:
        return f"Node: {self.value}"

    def visit(self):
        print(self.__repr__())


class Graph:
    def __init__(self, directed=False):
        self.nodes = set([Node])
        self.directed = directed

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_nodes(self, *nodes) -> None:
        for node in nodes:
            self.add_node(node)

    def bread_first_search(self, starting_node):
        queue = Queue()
        queue.enqueue(starting_node)

        discovered = set()
        discovered.add(starting_node)
        for node in queue:
            node.visit()
            for adj_node in node.adjacent_nodes:
                print(f"Visiting edge ({node.value},{adj_node.value})")
                if adj_node not in discovered:
                    queue.enqueue(adj_node)
                    discovered.add(adj_node)


g = Graph()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.add_adjacents(n3, n5)
n2.add_adjacents(n4, n5)
n3.add_adjacents(n1, n4)
n4.add_adjacents(n2, n3)
n5.add_adjacents(n1, n2)
g.add_nodes(n1, n2, n3, n4, n5)

q = Queue()
q.enqueue(n5)
q.enqueue(n2)
q.enqueue(n3)
q.enqueue(n1)
q.enqueue(n4)

g.bread_first_search(n5)
