import load_data_words as ldw
import operator

data_words = ldw.load_data()

# d = dict(data_words['misc.forsale'].most_common(50))
# s = float(sum(d.values()))
# for k in d:
#   d[k] = [d[k], d[k] / s]

# for k in reversed(sorted(d.items(), key=lambda x: x[1][0])):
#   print k
# print s


import os
from os import path
from collections import Counter
import pickle


data_path = 'test_data'

data_match = {}

for article_type in os.listdir(data_path):
  article_type_file_path = path.join(data_path, article_type)
  article_words = []
  for article in os.listdir(article_type_file_path):
    article_path = path.join(article_type_file_path, article)
    with open(article_path) as f:
      fc = f.read().splitlines()
      fcc = Counter(fc).most_common(50)
      print article_type, fcc

      s = float(sum(fcc.values()))

      for word in dict(fcc):
        ptf = fcc[word] / s
        

