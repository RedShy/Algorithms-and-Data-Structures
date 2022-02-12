#Albero binario di ricerca

class BinaryTree:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def find_min(self):
		if self.left is None:
			return self.value

		return self.left.find_min()

	def find_max(self):
		if self.right is None:
			return self.value

		return self.right.find_max()

	def find_value(self, value):
		if self.value == value:
			return True

		if value < self.value:
			if self.left is None:
				return False

			self.left.find_value(value)

		if value > self.value:
			if self.right is None:
				return False

			self.right.find_value(value)

	def print_elements(self):
		if self.left is not None:
			self.left.print_elements()

		print(self.value)

		if self.right is not None:
			self.right.print_elements()

	def add_order(self, value):
		if value <= self.value:
			if self.left is not None:
				self.left.add_order(value)
			else:
				self.left = BinaryTree(value)
				

		if value > self.value:
			if self.right is not None:
				self.right.add_order(value)
			else:
				self.right = BinaryTree(value)
				

	def get_height(self):
		left_height = 0
		if self.left is not None:
			left_height = self.left.get_height()

		right_height = 0
		if self.right is not None:
			right_height = self.right.get_height()

		return max(left_height, right_height) + 1

	def remove_element(self, value):
		if value == self.value:
			if self.has_no_child():
				self.value = None
				return 

			if self.left is not None and self.right is None:
				self.value = self.left.value
				if self.left.has_no_child():
					self.left = None
				else:
					self.left.remove_element(self.value)
				return

			if self.right is not None and self.right is None:
				self.value = self.right.value
				if self.right.has_no_child():
					self.right = None
				else:
					self.right.remove_element(self.value)
				return 

			# prendi il più a sinistra del lato destro
			self.value = self.right.find_min()
			if self.right.has_no_child():
				self.right = None
			else:
				self.right.remove_element(self.value)
		elif value < self.value:
			if self.left is not None:
				if self.left.has_no_child() and self.left.value == value:
					self.left = None
				else:
					self.left.remove_element(value)
			else:
				raise Exception("Value not found")
		elif value > self.value:
			if self.right is not None:
				if self.right.has_no_child() and self.right.value == value:
					self.right = None
				else:
					self.right.remove_element(value)
			else:
				raise Exception("Value not found")

	def has_no_child(self):
		return self.left is None and self.right is None

	def pop_min(self):
		min_value = self.find_min()
		self.remove_element(min_value)

		return min_value

	def pop_max(self):
		max_value = self.find_max()
		self.remove_element(max_value)

		return max_value


tree = BinaryTree(2)
tree.add_order(1)
tree.add_order(4)
tree.add_order(3)
tree.print_elements()
print()

print(tree.pop_min())
print(tree.pop_min())
print(tree.pop_min())
print(tree.pop_min())





