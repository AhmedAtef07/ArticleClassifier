# Run this file independently, to generate 'words_counted.data'.
# Only use load_data_words.py in the project.

import os
from os import path
from collections import Counter
import pickle


data_path = 'train_data'

data_words = {}

for article_type in os.listdir(data_path):
  article_type_file_path = path.join(data_path, article_type)
  article_words = []
  for article in os.listdir(article_type_file_path):
    article_path = path.join(article_type_file_path, article)
    with open(article_path) as f:
      fc = f.read().splitlines()
      article_words.extend(fc)
  data_words[article_type] = Counter(article_words)

# print data_words

with open('words_counted.data', 'wb') as output_file:
  pickle.dump(data_words, output_file, pickle.HIGHEST_PROTOCOL)

# not_alpha_count = 0
# for w in c:
#   if not w.isalpha():
#     # print w
#     not_alpha_count += 1
 
# print not_alpha_count