import difflib
import heapq
import operator
import json

"""
SequenceMatcher(None,a,b), difflib modülü altında gelen bir sınıftır. 
Dizileri karşılaştırmak için sınıflar ve işlevler sağlar.
Get yöntemi verilen anahatar değeri döndürür.
"""


def possibleAnswer(faq, question):
    distances = {}
    for key, value in faq.items():
        distances[key] = 0
        for key2, value2 in value.items():
            value2 = str(value2).capitalize()
            s = difflib.SequenceMatcher(lambda x: x == " ", question, value2)
            d = round(s.ratio(), 3)
            if distances[key] < d:
                distances[key] = d

    # kıysalma algoritmasında verilerin ön elemeden geçirerek oranın 0.4 ten küçüklerin elenmesi
    oran = (max(distances.items(), key=operator.itemgetter(1)))[1]
    if oran > 0.4:
        # en yüksek iki değer döndürülmesi için sıralanıp ilk iki değer kaydediliyor ve key olarak atanır
        enYuksekİkiDeger = heapq.nlargest(2, distances.items(), key=operator.itemgetter(1))
        key = enYuksekİkiDeger

    # kullanıcın sorduğu sorunun veri tabanında olmaması durumunda emptyQueryData.js dosyasına verilein kayıdı ile verilerin saklanması
    else:
        with open('./Data/EmptyQueryData.json') as file:
            data = json.load(file)
        for key, value in data.items():
            key = int(key) + 1

        dataveri = {key: question}
        data.update(dataveri)

        with open('./Data/EmptyQueryData.json', 'w') as file:
            json.dump(data, file)

        key = []
    return key