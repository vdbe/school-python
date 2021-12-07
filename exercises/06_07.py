#!/usr/bin/env python3

# sentence = input().strip()
sentence = "This is a nice sentence"
words = sentence.split()

length_longest_word = len(max(words, key=len))

[print(word.rjust(length_longest_word)) for word in words]
