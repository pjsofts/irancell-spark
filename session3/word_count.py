sentence = 'salam hi hello yes no hi hello'
words = sentence.split(' ')
print(words)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)