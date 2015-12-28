import pickle

def load_data():
  data_words = {}

  with open('words_counted.data', 'rb') as input_file:
    data_words = pickle.load(input_file)

  return data_words


# print data_words

# not_alpha_count = 0
# for w in c:
#   if not w.isalpha():
#     # print w
#     not_alpha_count += 1
 
# print not_alpha_count