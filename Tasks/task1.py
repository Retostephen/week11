word = "prp"

for a in range(len(word)):
	count = 0
	for b in range(len(word)):
		if word[a] == word[b]:
			count += 1
	if count == 1:
