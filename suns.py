import nltk
import numpy as np 
import re
from sklearn.datasets import load_files
import pickle
import requests
from sklearn import svm


nltk.download('stopwords') 
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# words = ['At', 'eight']
# gibberish = []

# sentence = "At eight o'clock on Thursday morning Kim didn't feel very good"
# tokens = nltk.word_tokenize(sentence)
# print(tokens)

# tagged = nltk.pos_tag(tokens)
# print(tagged[0:6])
# print(tagged)


#clasify if a word is a word or not a word
# isWords = []
# notWords = []

# response = requests.get("https://most-common-words.herokuapp.com/api")
# print(response.json())






