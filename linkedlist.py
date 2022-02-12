class Node:
	def __init__(self, value, next_node):
		self.value = value
		self.next = next_node

	def add_node(self, node):
		node.next = self.next
		self.next = node

class List:
	def __init__(self, start_node=None):
		self.start_node = start_node
		self.end_node = start_node

	def print_values(self):
		node = self.start_node
		while(node != None):
			print(node.value)
			node = node.next

	def add_node(self, node):
		if self.start_node:
			self.start_node.add_node(node)
		else:
			self.start_node = node

	def add_node_preserv_order(self, node):
		if self.start_node:
			self.find_last_node().add_node(node)
		else:
			self.start_node = node

	def find_last_node(self) -> Node:
		node = self.start_node
		while node.next != None:
			node = node.next

		return node

	def push_back(self, node):
		if self.end_node:
			self.end_node.add_node(node)
			self.end_node = node
		else:
			self.start_node = node
			self.end_node = node

	def is_present(self, value):
		node = self.start_node
		while node != None:
			if node.value == value:
				return True
			node = node.next

		return False

	def pop_back(self) -> Node:
		# 0 elements
		if self.start_node is None:
			raise Exception("pop on empty list")

		# 1 element
		if self.start_node == self.end_node:
			node = self.start_node
			self.start_node = None
			self.end_node = None
			return node

		# >1 elements
		node = self.start_node
		while node.next != self.end_node:
			node = node.next
		self.end_node = node

		return self.end_node.next

	def find_node(self, value) -> Node:
		node = self.start_node
		while node != None:
			if node.value == value:
				return node
			node = node.next
		return None

	def find_and_add(self, value, node_to_add):
		node = self.find_node(value)
		if node == None:
			raise Exception("Value not found")

		node.add_node(node_to_add)
		if node == self.end_node:
			self.end_node = node_to_add







linked_list = List()
linked_list.push_back(Node(1, None))
linked_list.push_back(Node(2, None))
linked_list.push_back(Node(3, None))
linked_list.push_back(Node(4, None))
linked_list.print_values()

linked_list.find_and_add(2, Node(11, None))
linked_list.print_values()
print()

linked_list.find_and_add(4, Node(15, None))
linked_list.print_values()
print()

linked_list.find_and_add(1, Node(13, None))
linked_list.print_values()
print()

linked_list.find_and_add(0, Node(14, None))






