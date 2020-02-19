import heapq
import operator

"""
Jaccard Benzerliği iki kümenin kesişiminin(xny) eleman sayısının birleşiminin kesişiminden 
çıkarılması çıkan sonucun bölümüdür
Jac(x,y)=(xny)/(|x|+|y|-|xny|)                   
"""


def get_jaccard_sim(Data, question):
    distances = {}
    for key, value in Data.items():
        distances[key] = 0
        for key2, value2 in value.items():
            if key2 == "faq":
                a = set(str(value2).lower().split())
                b = set(question.split())
                c = a.intersection(b)
                d = float(len(c)) / (len(a) + len(b) - len(c))
                if distances[key] < d:
                    distances[key] = d

    oran = (max(distances.items(), key=operator.itemgetter(1)))[1]
    if oran > 0.3:
        enYuksekİkiDeger = heapq.nlargest(2, distances.items(), key=operator.itemgetter(1))
        key = enYuksekİkiDeger
    else:
        key = []
    return key
