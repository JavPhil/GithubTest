def mid(word):
	offset = int(len(word) / 2)
	if len(word) % 2 == 0:
		return ""
	else:
		middle = word[offset: offset + 1]
	return(middle)

print(mid("abcde"))
print(mid("turtles"))
print(mid(""))
print(mid("abba"))
