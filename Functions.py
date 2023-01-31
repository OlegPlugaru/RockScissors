# Functions

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

#talk("I am going to buy the milk")

def count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()

#count()

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()
for i in range(10):
    print(count())
