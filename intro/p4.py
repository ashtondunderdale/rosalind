str = "We tried list and we tried dicts also we tried Zen"

words = {}
splitStr = str.split(' ')

for s in splitStr:
    if s not in words:
        words[s] = 0

    words[s] += 1

for s in words:
    print(s, words[s])