#!/usr/bin/env python3

# sentence = input()
sentence = "Python is great, it is the best scripting language in the world, and we love to learn it!"

d = {}

for word in sentence.split():
    d[word] = sentence.count(word)

print(d)
