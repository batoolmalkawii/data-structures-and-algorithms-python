import re

def repeared_word(input_string):
    count_dict = {}
    input_string = remove_punctuation(input_string).lower()
    words = input_string.split()

    for word in words:
        count_dict[word] = 0

    for word in words:
        count_dict[word] += 1

        if count_dict[word] > 1:
            print (count_dict)
            return (word)

    return (None)

def remove_punctuation(input_string):
    return (re.sub(r'[^\w\s]','',input_string))







if __name__ == "__main__":
    print(repeared_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))