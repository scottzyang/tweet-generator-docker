import sys
import random

def rearrange(arg_list):
    word_list = arg_list[1:]
    random.shuffle(word_list)
    new_string = ' '.join(word_list)
    return new_string


if __name__ == '__main__':
    new_string = rearrange(sys.argv)
    print(new_string)
