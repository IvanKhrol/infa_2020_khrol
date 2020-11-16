s = input()
s = s.replace(",", "")
s = s.replace(":", "")
s = s.replace(".", "")
s = s.lower()
s = s.split()
words = {}
for i in range(len(s)):
    x = s[i]
    if words.get(x) != None:
        words[x] += 1
    else:
        words.setdefault(x, 1)
list_words = list(words.items())
list_words.sort(key = lambda i: i[1])
list_words.reverse()
for i in list_words:
    print(i[0], ':', i[1])
    