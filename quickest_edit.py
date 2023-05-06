def skip(s, i):
	return s[:i] + s[i+1:]

def insert_to_dict(w, arr):
	for i in range(len(w)):
		new_w = skip(w, i)
		insert_to = arr[i]
		l = insert_to.get(new_w, [])
		l.append(w)
		insert_to[new_w] = l

def prep_dict_with_skips(list_of_words, word_len):
	dict_with_all_skips = [{} for i in range(word_len)]
	for w in list_of_words:
		insert_to_dict(w, dict_with_all_skips)

	return dict_with_all_skips



def quickest_edit(list_of_words, word_len, from_word, to_word):
	dict_with_all_skips = prep_dict_with_skips(list_of_words, word_len)

	stack = [(from_word, 0, [from_word])]

	seen_words = set()

	while(len(stack) > 0):
		(word, dist, trace) = stack.pop()
		for i in range(word_len):
			new_s = skip(word, i)
			read_from = dict_with_all_skips[i]
			list_of_neighbors = read_from.get(new_s)
			for neighbor in list_of_neighbors:
				if neighbor in seen_words or neighbor == word:
					continue

				seen_words.add(neighbor)
				if neighbor == to_word:
					return (trace + [to_word], dist+1)

				stack.append((neighbor, dist+1, trace + [neighbor]))

	return -1



print(quickest_edit(['abc', 'azd', 'abd', 'gbc', 'afd', 'bbd', 'bfd', 'bff'], 3, 'abc', 'bff'))
