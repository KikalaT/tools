# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import re
import sys
from spacy.lang.fr import French
from wordcloud import WordCloud


text = open(sys.argv[1]).read()

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = French()

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)

# Create list of word tokens
token_list = []
for token in my_doc:
	token_list.append(token.text)

from spacy.lang.fr.stop_words import STOP_WORDS

# Create list of word tokens after removing stopwords
filtered_sentence = '' 

for word in token_list:
	lexeme = nlp.vocab[word]
	if lexeme.is_stop == False:
		filtered_sentence += word+' ' 

# Generate a word cloud image
wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
wc.generate(filtered_sentence)

# store to file
#if sys.argv[2]:
#	wc.to_file(sys.argv[2])

# Display the generated image:
# the matplotlib way:
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
