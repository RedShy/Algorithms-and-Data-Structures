from heap import heapsort

def binary_search_left(elements, start, end, value):
	if not elements or start > end:
		return False

	middle_index = start + (end - start) // 2
	middle_value = elements[middle_index]
	if value == middle_value:
		return True

	if value < middle_value:
		return binary_search_left(elements, start, middle_index - 1, value)
	else:
		return binary_search_left(elements, middle_index + 1, end, value)

def binary_search_right(elements, start, end, value):
	if not elements or start > end:
		return False

	middle_index = start + (end - start) // 2
	middle_value = elements[middle_index]
	if value == middle_value:
		return True

	if value > middle_value:
		return binary_search_right(elements, start, middle_index - 1, value)
	else:
		return binary_search_right(elements, middle_index + 1, end, value)

def is_sorted(elements):
	for i in range(0, len(elements) - 2, 1):
		if elements[i + 1] < elements[i]:
			return False

	return True


A = [1, 6, 4, 2, 9, 10, 12, 4]

A_sorted = heapsort(A)
print(A_sorted[::-1])
print(binary_search_left(A_sorted[::-1], 0, len(A_sorted) - 1, 10))