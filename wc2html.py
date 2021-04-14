# -*- coding: utf-8 -*-

import base64
import random
import matplotlib.pyplot as plt
import re
import sys

from spacy.lang.fr import French
from wordcloud import WordCloud


text = open('/home/jericho/Bureau/jimtry.txt').read()

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
filename = ''
x = random.sample('0123456789',5)
for i in x:
	filename += i

wc.to_file('/home/jericho/Bureau/'+filename+'.png')
input_file = open('/home/jericho/Bureau/'+filename+'.png','rb').read()

png_encoded = str(base64.b64encode(input_file))
png_encoded = re.sub('b\'','', png_encoded)
png_encoded = re.sub('\'','', png_encoded)

html_content = '<html><body>'
html_content += '<img height="400" width="600" src="data:image/png;base64,'+png_encoded+'">'
html_content += '</body></html>'

output_file = open('/home/jericho/Bureau/'+filename+'.html','w')

output_file.write(html_content)
