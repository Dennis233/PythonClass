import string
from nltk.corpus import stopwords


# 定义一个函数getWords，用于读取文件中的文本，并将其转换为小写，然后将其中的标点符号替换为空格，最后将文本分割为单词列表
def getWords():
    f = open("hamlet.txt").read()  # Read the contents of the file
    txt = f.lower()  # Convert the text to lowercase
    for i in string.punctuation:
        txt = txt.replace(i, ' ')
    return txt.split()


# 定义一个函数countWords，用于统计单词出现的次数
def countWords(words):
    # 获取英文停用词表
    sw = stopwords.words('english')
    # 将停用词从words中移除
    words = [i for i in words if i not in sw]
    # 创建一个字典，用于存储单词及其出现的次数
    counts = {}
    # 遍历words，统计每个单词出现的次数
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    # 返回一个列表，其中包含每个单词及其出现的次数
    return list(counts.items())


# 定义一个函数sortWords，用于对传入的列表iterms进行排序
def sortWords(iterms: list):
    # 使用列表的sort方法对iterms进行排序，以x[1]为关键字，reverse=True表示降序排序
    iterms.sort(key=lambda x: x[1], reverse=True)
    # 遍历iterms，打印出前10个元素
    for i in range(10):
        word, count = iterms[i]
        print('{0:<10}:{1:>5}'.format(word, count))


# 调用函数getWords，获取helmet_words
helmet_words = getWords()
# 调用函数countWords，获取helmet_count
hemlet_count = countWords(helmet_words)
# 调用函数sortWords，对helmet_count进行排序
sortWords(hemlet_count)
