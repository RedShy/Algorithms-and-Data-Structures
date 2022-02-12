def mergesort(list, start, end):
	if not list or start > end or start < 0 or end >= len(list):
		return list

	if start == end:
		return [list[start]]

	middle_index = start + (end - start) // 2
	sorted_A = mergesort(list, start, middle_index)
	sorted_B = mergesort(list, middle_index + 1, end)

	return merge(sorted_A, sorted_B)

def merge(sorted_A, sorted_B):
	i_A = 0
	i_B = 0
	sorted_final = []
	while i_A < len(sorted_A) and i_B < len(sorted_B):
		if sorted_A[i_A] <= sorted_B[i_B]:
			sorted_final.append(sorted_A[i_A])
			i_A += 1
		else:
			sorted_final.append(sorted_B[i_B])
			i_B += 1

	while i_A < len(sorted_A):
		sorted_final.append(sorted_A[i_A])
		i_A += 1

	while i_B < len(sorted_B):
		sorted_final.append(sorted_B[i_B])
		i_B += 1

	return sorted_final


print(mergesort([11,1,44,3,77,1,0,44,2,7], 0, 6))