#! /usr/bin/env python
import nltk
import sys


def process1(s):
	tokens = nltk.word_tokenize(s)
	tagged = nltk.pos_tag(tokens)
	grammar = r"""
	
	NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  	PP: {<IN><NP>}               # Chunk prepositions followed by NP
  	VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
	PATH: {<NP><VB.*><NP>}
  	CLAUSE: {<NP><VP>}           # Chunk NP, VP
	"""
	# NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
    #   {<NNP>+}                # chunk sequences of proper nouns
	
	#NP: {<DT>?<JJ>*<NN>+}
	cp = nltk.RegexpParser(grammar)
	entities = cp.parse(tagged)
	# entities = nltk.chunk.ne_chunk(tagged)
	return entities

def process2(s):
	tokens = nltk.word_tokenize(s)	
	tagged = nltk.pos_tag(tokens)

	grammar = nltk.parse_cfg("""
		S -> NP VP
		PP -> P NP
		NP -> Det N | Det N PP | 'I'
		VP -> V NP | VP PP
 		Det -> 'an' | 'my'
 		N -> 'elephant' | 'pajamas'
		V -> 'shot'
		P -> 'in'
	""")
	parser = nltk.ChartParser(grammar)
	trees = parser.nbest_parse(tagged)
	return trees

# print("Hello nltk")
#process 1
text1 = """
	Patients that receive chemotherapy and are female
"""
text2 = """
	Clinical Trial recruits patient that suffers disease
"""

text3 = """
	Patient undergoes a biopsy, which reveals a sample that has size. The biopsy happens before chemotherapy
"""
if len(sys.argv) > 2 :
	ent = process1(sys.argv[1])
	# ent.draw()
	print(ent)

else:
	ent = process1(text1)
	# ent.draw()
	print(ent)

	ent = process1(text2)
	# ent.draw()
	print(ent)

	ent = process1(text3)
	# ent.draw()
	print(ent)


#process 2
# trees = process2(sys.argv[1])
# for tree in trees:
# 	tree.draw()
# 	print tree

# Patient undergoes a biopsy, which reveals a sample that has size. The biopsy happens before chemotherapy