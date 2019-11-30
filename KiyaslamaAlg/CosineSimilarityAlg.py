import heapq
import re, math
import operator
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


"""
Kosinüs benzerliği , aralarındaki açının kosinüsünü ölçen, iç çarpım uzayının sıfır olmayan 
iki vektörü arasındaki benzerliğin bir ölçüsüdür.
Cosine = (AB) / (|| A ||. || B ||) ki burada A ve B vektörlerdir.
"""


def CosineSimilarity(Data, question):
    distances = {}
    for key, value in Data.items():
        distances[key] = 0
        for key2, value2 in value.items():
            if key2 == "faq":
                value2 = str(value2).capitalize()
                vector1 = text_to_vector(value2)
                vector2 = text_to_vector(question)
                cosine = get_cosine(vector1, vector2)
                if distances[key] < cosine:
                    distances[key] = cosine

    oran = (max(distances.items(), key=operator.itemgetter(1)))[1]
    if oran > 0.4:
        enYuksekİkiDeger = heapq.nlargest(2, distances.items(), key=operator.itemgetter(1))
        key = enYuksekİkiDeger
    else:
        key = []
    return key
