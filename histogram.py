import sys
import random

import sys
import timeit
import string
from collections import defaultdict

def histogram(filename):
  # initialize empty histogram
  histogram = {}
  # verify command line args.
    # take filename and open as file
  with open(filename) as file:
    # read file, remove puncuation, and convert to array
    word_list = file.read().translate(str.maketrans('', '', string.punctuation)).lower().split()

    # loop through words
    for word in word_list:
      # increment if word exists
      if histogram.get(word):
        histogram[word] += 1
      else:
        # add new word count
        histogram[word] = 1
  return histogram

def unique_words(histogram):
  # return the length of the dictionary
  return len(histogram)

def frequency(word, histogram):
  # find word in histogram, else return error statement.
  # if type(histogram) is list:
  #   for entry in histogram:
  #     if entry[0] == word:
  #       return entry[1]
  # return f'Inputted word "{word}" was not found in histogram.'
  freq_dict = defaultdict(int)
  freq_dict.update(histogram)
  return freq_dict.get(word, 0)



# random word based on uniform distribution
def random_word(histogram):
  # convert histogram keys to list and grab random key
  random_word = random.choice(list(histogram.keys()))
  return random_word

import timeit

# random word based on weight distribution
def weighted_word(histogram):
  # convert keys to list
  keys = list(histogram.keys())
  # convert values to list
  values = list(histogram.values())
  # return random word based on weights
  random_word = random.choices(keys, values)[0]

  return random_word

def random_sentence(histogram):
  new_sentence = []
  word_count = random.randrange(15, 30)
  for i in range(word_count):
    # select random word
    rand_word = weighted_word(histogram)
    # capitalize first letter
    if len(new_sentence) == word_count - 1:
      rand_word += "."
    new_sentence.append(rand_word)
  return " ".join(new_sentence).capitalize()


if __name__ == '__main__':
  # create histogram and initialize stats counter
  count = {}
  histogram = histogram("michael_scott.txt")

  sentence = random_sentence(histogram)
  print(sentence + "\n")

  # evaluate run time
  total_time = 0
  iterations = 10000

  for i in range(iterations):
    elapsed_time = timeit.timeit(lambda: random_sentence(histogram), number=1)
    total_time += elapsed_time

  print(f'Total run time: {total_time}.\n')

  def counter(word):
    if count.get(word):
      count[word] += 1
    else:
      count[word] = 1

  # determine weighted probability stats
  for i in range(1000):
    # grab weighted word selection
    word = weighted_word(histogram)
    # add word to stats counter
    counter(word)
  print(f'Weighted Stats:\n{count}')



