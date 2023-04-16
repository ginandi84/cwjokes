from random import randrange

def rand_derangement(l):
	n = len(l)
	helper = list(range(n))

	elem = l[0] 
	index_in_helper = randrange(1, n)
	index_from_helper = helper[index_in_helper]

	while n > 1:
		next_elem = l[index_from_helper]
		l[index_from_helper] = elem
		elem = next_elem
		helper[index_in_helper] = helper[n-1]
		n = n - 1

		if (n == 1):
			l[0] = elem

		else:
			index_in_helper = randrange(1, n)
			index_from_helper = helper[index_in_helper]

	return l
