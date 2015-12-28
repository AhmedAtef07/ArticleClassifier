from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("data"):
  # dirpath.remove("data")
  print type(dirpath)
  # f.extend(filenames)
# print f  