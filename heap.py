#Implementare binary heap con lista
#Implementare metodo add element
#Implementare metodo get min/max (a seconda se è min heap o max heap)

class MaxHeap:
	def __init__(self):
		self.elements = list()

	def add(self, value):
		# aggiungo l'elemento
		self.elements.append(value)

		self.check_root(len(self.elements) - 1)


	def check_root(self, index):
		if index == 0:
			return

		# qual è la tua root?
		root_index = int(index / 2 - 0.5)

		if self.elements[index] > self.elements[root_index]:
			self.elements[root_index], self.elements[index] = self.elements[index], self.elements[root_index]

		self.check_root(root_index)

	def is_heap(self):
		for i, e in enumerate(self.elements):
			if i * 2 + 1 >= len(self.elements):
				break

			if i * 2 + 2 >= len(self.elements):
				break

			if e < self.elements[i*2 + 1] or e < self.elements[i*2 + 2]:
				return False

		return True

	def get_max(self):
		if not self.elements:
			return None

		max = self.elements[0]
		if len(self.elements) == 1:
			self.elements.pop()
			return max

		self.elements[-1], self.elements[0] = self.elements[0], self.elements[-1]
		self.elements.pop()

		self.check_child(0)

		return max

	def check_child(self, index):
		child = None
		if index * 2 + 1 < len(self.elements):
			child = index * 2 + 1

		if index * 2 + 2 < len(self.elements):
			if child is None or self.elements[index * 2 + 2] > self.elements[index * 2 + 1]:
				child = index * 2 + 2

		if child is None:
			return

		if self.elements[child] > self.elements[index]:
			self.elements[child], self.elements[index] = self.elements[index], self.elements[child]
			self.check_child(child)


def heapsort(elements):
	heap = MaxHeap()
	for e in elements:
		heap.add(e)
	list_sorted = list()
	for i in range(len(heap.elements)):
		list_sorted.append(heap.get_max())

	return list_sorted



#heap = MaxHeap()
#heap.add(8)
#heap.add(2)
#heap.add(5)
#heap.add(1)
#heap.add(3)
#heap.add(1)
#heap.add(1)
#heap.add(5)
#print(heap.elements)
#print(f"Is really an heap? {heap.is_heap()}")

#print(heap.get_max())
#print(heap.elements)
#print(f"Is really an heap? {heap.is_heap()}")


