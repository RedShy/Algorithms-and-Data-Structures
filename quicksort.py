import random

def quicksort(list, start, end):
	if start >= end:
		return

	pivot_index = random.randint(start, end)
	pivot = list[pivot_index]

	higher_than_pivot = []
	lower_than_pivot = [] 
	for i in range(start, end + 1):
		if i == pivot_index:
			continue

		if list[i] > pivot:
			higher_than_pivot.append(list[i])
		else:
			lower_than_pivot.append(list[i])

	lower_than_pivot.append(pivot)
	pivot_index = start + len(lower_than_pivot) - 1
	final_list = lower_than_pivot + higher_than_pivot
	for i in range(len(final_list)):
		list[start + i] = final_list[i]

	quicksort(list, start, pivot_index - 1)
	quicksort(list, pivot_index + 1, end)

A = [1,5,2,0,11,22,4,55,2,9,0,12]
quicksort(A, 0, len(A) - 1)
print(A)






