import string
from nltk.corpus import stopwords


def getWords():
    f = open("hamlet.txt").read()  # Read the contents of the file
    txt = f.lower()  # Convert the text to lowercase
    for i in string.punctuation:
        txt = txt.replace(i, ' ')
    return txt.split()


def countWords(words):
    sw = stopwords.words('english')
    words = [i for i in words if i not in sw]
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return list(counts.items())


def sortWords(iterms: list):
    iterms.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = iterms[i]
        print('{0:<10}:{1:>5}'.format(word, count))


helmet_words = getWords()
hemlet_count = countWords(helmet_words)
sortWords(hemlet_count)
