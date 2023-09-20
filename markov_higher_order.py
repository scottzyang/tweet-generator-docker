import random
import string
import json
import timeit
from collections import deque

class Markovgram():
  def __init__(self, source_text, tuple_length):
    self.words_list = self._process_text(source_text)
    self.markov_chain = {}
    self.random_sentence = []
    self.tuple_length = tuple_length

  # read file into list of strings.
  def _process_text(self, source_text):
    # take file and open as a read file, remove punctuation, and convert to list.
    with open(source_text) as file:
      words = file.read().translate(str.maketrans('', '', string.punctuation)).lower().split()
      return words

  # loop through list and create dict[dict]
  def generate_markov_chain(self):
    if self.tuple_length >= len(self.words_list):
      raise Exception("Tuple length cannot be larger than or equal to words list length.")

    # double ended queue
    window = deque()

    # stop one before the end to avoid indexing out of list
    for window_end in range(len(self.words_list) - 1):
      # add element to window
      window.append(self.words_list[window_end])

      # create tuple once window limit is reached
      if window_end >= self.tuple_length - 1:
        # convert to tuple
        key = tuple(window)
        # eval if tuple exists in MC
        if not self.markov_chain.get(key):
          self.markov_chain[key] = {}

        # set next word
        next_word = self.words_list[window_end + 1]
        # find existing frequency of word after tuple else return 0
        frequency = self.markov_chain[key].get(next_word, 0)
        # increment frequency by 1
        self.markov_chain[key][next_word] = frequency + 1

        # remove first element from window to maintain tuple length
        window.popleft()

  # eval markov chain and create sentence
  def create_sentence(self):
    # get list of keys
    tuple_keys = list(self.markov_chain.keys())
    # select random tuple
    current_tuple = random.choice(tuple_keys)
    # convert tuple to list and append to sentence
    self.random_sentence.extend(current_tuple)
    # random sentence length
    word_count = random.randrange(15, 20)

    for i in range(word_count):
      # find current tuple in MC
      nested_dict = self.markov_chain.get(tuple(current_tuple))

      if nested_dict:
        words = list(nested_dict.keys())
        weights = list(nested_dict.values())

        # choose most frequent word
        next_word = random.choices(words, weights)[0]
        self.random_sentence.append(next_word)

        # convert to deque
        current_tuple = deque(current_tuple)
        # remove first element
        current_tuple.popleft()
        # add next word to tuple
        current_tuple.append(next_word)

    self.random_sentence = " ".join(self.random_sentence).capitalize() + "."

if __name__ == '__main__':
  fishy = Markovgram("stats.txt", 0)

  # # print(fishy.words_list)
  fishy.generate_markov_chain()

  print(fishy.markov_chain)

  fishy.create_sentence()

  print(fishy.random_sentence)
