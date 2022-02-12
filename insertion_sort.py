import random

def insert_in_ordered_list(A, index_value):
	for i in range(index_value - 1, -1, -1):
		if A[i] > A[index_value]:
			A[index_value], A[i] = A[i], A[index_value]
		elif A[i] <= A[index_value]:
			break 
		index_value -= 1

def insertion_sort(A):
	for i in range(1, len(A), 1):
		insert_in_ordered_list(A, i)

	return A

A = [1,6,4,2,5,6,9,10,12]
random.shuffle(A)

print(insertion_sort(A))