#! /usr/bin/env python
import nltk
from nltk.corpus import brown
import sys
import pickle
import os.path

def printAccuracy(tagger, test):
	print 'Accuracy: %4.1f%%' % (
		100.0 * tagger.evaluate(test))

def printTAGS(tags):
	print
	print tags
	last = ''
	for w in tags:
		if w[1].startswith("N"):
			if last == 'c':
				print 'NEW PATH'
			print "<CLASS>{0}</CLASS>".format(w[0])
			last = 'c'
		if w[1].startswith("V") or w[1].startswith("HVZ")or w[1].startswith("BER") : 
			print "<PROPERTY>{0}</PROPERTY>".format(w[0])
			last = 'p'

	print		

def tagger_training():
	brown_news_tagged = brown.tagged_sents(categories=['news', 'editorial', 'learned', 'reviews'])
	# brown_news_tagged = brown.tagged_sents(categories=['news', 'learned', 'reviews'])
	brown_train = brown_news_tagged[100:]

	regexp_tagger = nltk.RegexpTagger(
     [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
      (r'(The|the|A|a|An|an)$', 'AT'),   # articles
      (r'.*able$', 'JJ'),                # adjectives
      (r'.*ness$', 'NN'),                # nouns formed from adjectives
      (r'.*ly$', 'RB'),                  # adverbs
      (r'.*s$', 'NNS'),                  # plural nouns
      (r'.*ing$', 'VBG'),                # gerunds
      (r'.*ed$', 'VBD'),                 # past tense verbs
      (r'.*', 'NN')                      # nouns (default)
 	])
 	unigram_tagger_2 = nltk.UnigramTagger(brown_train, backoff=regexp_tagger)
 	bigram_tagger = nltk.BigramTagger(brown_train, backoff=unigram_tagger_2)
 	trigram_tagger = nltk.TrigramTagger(brown_train, backoff=bigram_tagger)

 	return trigram_tagger

def open_tagger():	
	training_file = 'my_tagger_training.pickle'
	if not os.path.isfile(training_file):
		f = open(training_file,'w')
		tagger = tagger_training()
		pickle.dump(tagger,f)
		f.close()
	else:
		#And then when you need to load the tagger you use:
		f = open(training_file,'r')
		tagger = pickle.load(f)
		f.close()

	return tagger
	


# brown_news_tagged = brown.tagged_sents(categories='news')
# brown_news_tagged = brown.tagged_sents(categories=['news', 'editorial', 'learned', 'reviews'])
# brown_news_tagged = brown.tagged_sents(categories=['news', 'learned', 'reviews'])
# brown_news_tagged = brown.tagged_sents()

# brown_news_text = brown.sents(categories='news')
# tagger = nltk.UnigramTagger(brown_news_tagged[:500])
# res1 = tagger.tag(brown_news_text[501])
# print 
# print res1
# printAccuracy(tagger, brown_news_tagged[:100])

#brown_train = brown_news_tagged[100:]
#brown_test = brown_news_tagged[:100]
#test_sent = nltk.tag.untag(brown_test[0])
test_sent1 = """
	Patients that receive chemotherapy and are female
"""
test_sent1 = test_sent1.split()

test_sent2 = """
	Clinical Trial recruits patient that suffers disease
"""
test_sent2 = test_sent2.split()

test_sent3 = """
	Patient undergoes a biopsy, which reveals a sample that has size. The biopsy happens before chemotherapy
"""
test_sent3 = test_sent3.split()


# DEFAULT TAGGER
# default_tagger = nltk.DefaultTagger('XYZ')
# res2 = default_tagger.tag('This is a test'.split())
# print 
# print res2

# default_tagger = nltk.DefaultTagger('NN')
# res3 = default_tagger.tag(test_sent)
# print 
# print res3
# printAccuracy(default_tagger, brown_test)

# regexp_tagger = nltk.RegexpTagger(
#      [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
#       (r'(The|the|A|a|An|an)$', 'AT'),   # articles
#       (r'.*able$', 'JJ'),                # adjectives
#       (r'.*ness$', 'NN'),                # nouns formed from adjectives
#       (r'.*ly$', 'RB'),                  # adverbs
#       (r'.*s$', 'NNS'),                  # plural nouns
#       (r'.*ing$', 'VBG'),                # gerunds
#       (r'.*ed$', 'VBD'),                 # past tense verbs
#       (r'.*', 'NN')                      # nouns (default)
#  ])
# print regexp_tagger.tag(test_sent1)
# printAccuracy(regexp_tagger, brown_test)

# UNIGRAM WO backoff
# unigram_tagger = nltk.UnigramTagger(brown_train)
# res5 = unigram_tagger.tag(test_sent) 
# printAccuracy(unigram_tagger, brown_test)

#unigram_tagger_2 = nltk.UnigramTagger(brown_train, backoff=regexp_tagger)
# print unigram_tagger_2.tag(test_sent1)
# print unigram_tagger_2.tag(test_sent2)
# print unigram_tagger_2.tag(test_sent3)
# printAccuracy(unigram_tagger_2, brown_test)

#bigram_tagger = nltk.BigramTagger(brown_train, backoff=unigram_tagger_2)
# print bigram_tagger.tag(test_sent1)
# print
# print bigram_tagger.tag(test_sent2)
# print
# print bigram_tagger.tag(test_sent3)
# printAccuracy(bigram_tagger, brown_test)

#trigram_tagger = nltk.TrigramTagger(brown_train, backoff=bigram_tagger)
# print
# print trigram_tagger.tag(test_sent1)
# print
# print trigram_tagger.tag(test_sent2)
# print
# print trigram_tagger.tag(test_sent3)
# printAccuracy(trigram_tagger, brown_test)

# tags = trigram_tagger.tag(test_sent1)
# printTAGS(tags)
# tags = trigram_tagger.tag(test_sent2)
# printTAGS(tags)
# tags = trigram_tagger.tag(test_sent3)
# printTAGS(tags)

tagger = open_tagger()
tags = tagger.tag(test_sent1)
printTAGS(tags)

tags = tagger.tag(test_sent2)
printTAGS(tags)

tags = tagger.tag(test_sent3)
printTAGS(tags)

print "FIN"


