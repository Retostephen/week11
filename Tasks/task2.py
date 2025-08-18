word = "ptr"
unique_character = []

for a in range(len(word)):
	count = 0
	for b in range(len(word)):
		if word[a] == word[b]:
			count += 1
	if count == 1:
		unique_character.append(word[a])
if len(unique_character) >= 2:
	print(f'The second unique character is: {unique_character[1]}')
