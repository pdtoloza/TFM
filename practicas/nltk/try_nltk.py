#! /usr/bin/env python
import nltk
import sys


def process(s):
	tokens = nltk.word_tokenize(s)
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	return entities

# print("Hello nltk")
print(process(sys.argv[1]))