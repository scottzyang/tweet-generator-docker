import random

quotes = ("Sometimes I'll start a sentence and I don't even know where it's going. I just hope I find it along the way. Like an improv conversation.",
          "I understand nothing.",
          "I am Beyoncé, always.",
          "I'm not superstitious...but I'm a little stitious.")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
