from nltk import tokenize
import random


def classify(text, theme):
    splittext = tokenize.sent_tokenize(text)

    highlighted = []

    #replaced with classifier

    for sentences in splittext:
        test = random.randint(1)
        if test == 0:
            highlighted.append(sentences)
    return highlighted
