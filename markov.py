import random
import string
import json
import timeit

class Markovgram():
  def __init__(self, source_text):
    self.words_list = self._process_text(source_text)
    self.markov_chain = {}
    self.random_sentence = []

  # read file into list of strings.
  def _process_text(self, source_text):
    # take file and open as a read file, remove punctuation, and convert to list.
    with open(source_text) as file:
      words = file.read().translate(str.maketrans('', '', string.punctuation)).lower().split()
      return words

  # loop through list and create dict[dict]
  def generate_markov_chain(self):
    for index, word in enumerate(self.words_list):
      # check if word exists as entry in markov chain
      if not self.markov_chain.get(word):
        # if not, create new blank entry
        self.markov_chain[word] = {}

      # check if curr key exists in prev key
      if index != 0:
        # grab previous markov entry using last index
        previous_entries = self.markov_chain.get(self.words_list[index - 1])
        # checking if word exist in entries
        if previous_entries.get(word):
          previous_entries[word] += 1
        else:
          previous_entries[word] = 1


  # eval markov chain and create sentence
  def create_sentence(self):
    # select random word from word list, add to random_sentence
    current_word = random.choice(self.words_list)
    self.random_sentence.append(current_word)

    # random sentence length
    word_count = random.randrange(15, 35)

    for i in range(word_count):
      # find word in markov chain
      nested_dict = self.markov_chain.get(current_word)

      # if dictionary is not empty
      if nested_dict:
        # eval nested dict and grab weighted word
        words = list(nested_dict.keys())
        weights = list(nested_dict.values())

        next_word = random.choices(words, weights)[0]
        self.random_sentence.append(next_word)
        current_word = next_word

    self.random_sentence = " ".join(self.random_sentence).capitalize() + "."

if __name__ == '__main__':
  fishy = Markovgram("michael_scott.txt")

  # # print(fishy.words_list)
  fishy.generate_markov_chain()

  # json_obj = json.dumps(fishy.markov_chain)
  # print(json_obj)

  fishy.create_sentence()

  print(fishy.random_sentence)

  # total_time = 0
  # iterations = 1000

  # for i in range(iterations):
  #   elapsed_time = timeit.timeit(lambda: Markovgram("michael_scott.txt"), number=1)
  #   total_time += elapsed_time

  # print(f'Total run time: {total_time}.\n')
