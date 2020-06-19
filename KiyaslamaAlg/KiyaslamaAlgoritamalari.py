from KiyaslamaAlg import CosineSimilarityAlg
from KiyaslamaAlg import JaccardAlg
from KiyaslamaAlg import SequenceMatcher
from KiyaslamaAlg import ExceleAktar

"""
Chatbot.py den gelen verileri bütün kıyaslama algoritmalarına gönderilir
gönderilen veriler doğrultusunda alınan veriler işlenerek son kullanıcıya iletilir.
yapılan adımlar ;
1: fonk. verileri gönder 
2: Gelen dizilerin kıyaslama oranlarının ortalamsını al 
3: listeyi düzenle
4: kullanıcıya cevap gönder
"""

def AlgoritmaCagir(JsonData, question):
    alg1 = SequenceMatcher.possibleAnswer(JsonData, question)
    alg2 = CosineSimilarityAlg.CosineSimilarity(JsonData, question)
    alg3 = JaccardAlg.get_jaccard_sim(JsonData, question)

    ExceleAktar.Excel(question,alg1,alg2,alg3)

    # print("Sequence"+str(alg1))
    # print("Cosine"+str(alg2))
    # print("Jacard"+ str(alg3)+"\n")

    # ortalama alınması için algoritmaların
    ortalama = Ortalama(alg1, alg2, alg3)
    print("Ortalama : " + str(ortalama))

    if ortalama != 0:
        # algoritmalardan gelen dizileri tek bir diziye ekleme
        liste = []
        liste.append(alg1)
        liste.append(alg2)
        liste.append(alg3)

        # listenin düzenlenmesi
        gonderilecekListe = gonder(liste)
        # key arayüz yapıldıgında chatbot.py dosyasına taşınacak ona göre listelenme yapılacak
        key = gonderilecekListe[0][0]
        print("Gösterilen key'in oranı :" + str(gonderilecekListe[0][1]))

    else:
        key = "Null"

    cevap = JsonData.get(str(key),'')
    return cevap.get("answer","")


"""
Kullanıcıya cevap göndermeden önce liste temizlenir ve içinde döndürülen cevaplar sıralanarak çogunluk 
oylaması yapılır ve aynı olan verilerin diziden çıkarılır, çıkarılan veri kadar +1 oy (oran) eklenir.
ve son listenin geri gönderilmesi gerçekleşir.
"""


def gonder(liste):
    yeniListe = []
    # iç içe olan liste temizlenir
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            ekle = [int(liste[i][j][0]),float(liste[i][j][1])]
            yeniListe.append(ekle)


    yeniListe = sorted(yeniListe, reverse=True)  # listeyi büyükten küçüge doğru sıralar

    # liste dolaşılarak aynı olan sonucu döndüren keylerin oranına 1 ekler
    for i in range(len(yeniListe)):
        for j in range(len(yeniListe)):
            if i < len(yeniListe)-1 and i < j and j < len(yeniListe):
                if yeniListe[i][0] == yeniListe[j][0]:
                    yeniListe[i][1] += float(1.00)
                    yeniListe.remove(yeniListe[j])
                    if yeniListe[i][0] == yeniListe[j][0]:
                        yeniListe[i][1] += float(1.00)
                        yeniListe.remove(yeniListe[j])

    yeniListe = sorted(yeniListe, reverse=True)  # listeyi büyükten küçüge doğru sıralar

    return yeniListe

"""
algoritmaların döndürdüğü oranların ortalamasının alındıgı fonksiyon
"""


def Ortalama(alg1, alg2, alg3):
    toplam = 0
    aratoplam = 0
    say = 0

    # Alg1 den gelen listenin boş olmaması durumunda calışır.
    if alg1 != []:
        for i in range(len(alg1)):
            aratoplam = (alg1[i][1] + aratoplam)
            say = say + 1

        toplam = aratoplam + toplam
    aratoplam = 0

    # Alg2 den gelen listenin boş olmaması durumunda calışır.
    if alg2 != []:
        for i in range(len(alg2)):
            aratoplam = (alg2[i][1] + aratoplam)
            say = say + 1

        toplam = aratoplam + toplam
    aratoplam = 0

    # Alg3 den gelen listenin boş olmaması durumunda calışır.
    if alg3 != []:
        for i in range(len(alg3)):
            aratoplam = (alg3[i][1] + aratoplam)
            say = say + 1
        toplam = aratoplam + toplam

    if say != 0:
        ortalama = toplam / say

    else:
        ortalama = 0

    return ortalama
