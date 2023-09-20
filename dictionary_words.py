import random
import sys

words_path = "/usr/share/dict/words"

def random_words(args):
  if len(args) == 2:
    number = int(args[1])

    with open(words_path) as file:
      word_list = file.read().splitlines()
      random_sample = random.sample(word_list, number)
      sentence = " ".join(random_sample)
      return sentence + "."
  else:
     return "Please pass in a valid word count."


if __name__ == '__main__':
    new_sentence = random_words(sys.argv)
    print(new_sentence)





'''
  pseudocode

dictionary func(number)
  open file
  Read lines and convert to list
  grab random sample of words based on input
  join words together into string
  print new sentence


'''
