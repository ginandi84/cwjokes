def get_all_permutations(input, prefix = []):
	n = len(input)
	if n == 0:
		return [prefix]

	result = []
	for i in range(n):
		element = input[i]
		new_prefix = prefix + [element]
		new_input = input[0:i] + input[i+1:]
		result.extend(get_all_permutations(new_input, new_prefix))

	return result


print(get_all_permutations([1,2,3]))
print(get_all_permutations([]))
