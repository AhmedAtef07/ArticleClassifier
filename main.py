import os
from os import path
from collections import Counter
import operator

import load_data_words as ldw
data_words = ldw.load_data()

# print data_words

article_types = data_words.keys()

TYPE_RECOGNIZER_WORDS_COUNT = 50;

def calulcate_freq_prob(d):
  type_recognizer_words = {}
  for article_type in d:
    # print article_type
    dwat = d[article_type]
    trw = dict(dwat.most_common(TYPE_RECOGNIZER_WORDS_COUNT))
    s = float(sum(dwat.values()))
    for k in trw:
      trw[k] = [trw[k], trw[k] / s]
    type_recognizer_words[article_type] = trw
  return type_recognizer_words

type_recognizer_words = calulcate_freq_prob(data_words);
# print type_recognizer_words

  # for k in reversed(sorted(trw.items(), key=lambda x: x[1][0])):
    # print k
  # print s

# print type_recognizer_words



# def match_with_saved_articles(article_path, article_words):
#   res = {}
#   for common_w in article_words: # will loop for wach word in the current article
#     # print common_w
#     for article in type_recognizer_words: # will loop on all saved articles
#       prob = 0.0
#       for article_common_w in type_recognizer_words[article]: # will get each word n each saved article
#         # print ">> ", type_recognizer_words[article]
#         if common_w in type_recognizer_words[article]: # will compare and calculare probabilty
#           # print  "'" + common_w + "' IS IN this array", type_recognizer_words[article].keys(), "<<<<<<<<<------"
#           # print "##", article_words[common_w][1], type_recognizer_words[article][common_w][1]
#           prob += article_words[common_w][1] * type_recognizer_words[article][common_w][1]
#         else: 
#           # print  "'" + common_w + "' is not in this array", type_recognizer_words[article].keys()
#           pass
#       res[article] = prob
#       # print res

#   print article_path

results = {}
def match_with_saved_articles(article_path, article_words):
  results[article_path] = {}
  for train_article in type_recognizer_words:
    prob = 0
    for train_word in type_recognizer_words[train_article]:
      for test_word in range(len(article_words)):
        if train_word in article_words.keys(): 
          prob += type_recognizer_words[train_article][train_word][1] * article_words[train_word][1]
        else:
          # print train_word, " word does not exist in ", article_words.keys()
          pass
    results[article_path][train_article] = prob


test_data_path = 'test_data'

def test_train_set():
  for article_type in os.listdir(test_data_path):
    article_type_file_path = path.join(test_data_path, article_type)
    for article in os.listdir(article_type_file_path):
      article_path = path.join(article_type_file_path, article)
      with open(article_path) as f:
        fwords = f.read().splitlines()
        # print len(fwords)
        fc = Counter(fwords)
        article_words = calulcate_freq_prob({article_type: fc})
        article_words = article_words[article_words.keys()[0]]

        # print article_path, article_words

        # here article_words contains each word in this test article.

        # print article_words
        ##################### START ALGORITHM ##################### 
        # First want to loop to get all previsuly calculated frequencies
        match_with_saved_articles(article_path, article_words)
        # return
        ###################### END ALGORITHM ###################### 
        


        # print article_type, article_words

test_train_set()

# print results

print "=" * 30

hit_count = 0
for k in results:
  should_be = k.split('/')[1]
  best_match, probability = list(reversed(sorted(results[k].items(), key=operator.itemgetter(1))))[0]
  is_hit = should_be == best_match
  if is_hit: hit_count += 1 
  print "[%5s] '%25s' '%25s' %f" % (is_hit, should_be, best_match, probability)

print "=" * 30

print "From %d test cases: %d is hit with accruacy %0.2f%%" % (len(results), hit_count, hit_count * 100.0 / len(results) )

# get each word from the current test artical
# calculate its frequency and probability of occurance in its article
# for loop on all the articles you have, multiply each probability by the probailbity of existence in that article
# add these probabilites together in some dict, sort them to find the matches.