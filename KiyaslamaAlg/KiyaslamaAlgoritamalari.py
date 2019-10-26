from KiyaslamaAlg import SequenceMatcher
from KiyaslamaAlg import CosineSimilarityAlg
from KiyaslamaAlg import JaccardAlg


"""
Chatbot.py den gelen verileri bütün kıyaslama algoritmalarına gönderilir
gönderilen veriler doğrultusunda alınan veriler işlenerek son kullanıcıya iletilir.
yapılan adımlar ;
1: fonk. verileri gönder 2: Gelen dizilerin kıyaslama oranlarının ortalamsını al 3: listeyi düzenle 4: kullanıcıya cevap gönder
"""

def AlgoritmaCagir(faq, answers, question):
    alg1 = SequenceMatcher.possibleAnswer(faq, question)
    alg2 = CosineSimilarityAlg.CosineSimilarity(faq, question)
    alg3 = JaccardAlg.get_jaccard_sim(faq, question)

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
        gonderilecekListe = gonder(liste, ortalama)
        # key arayüz yapıldıgında chatbot.py dosyasına taşınacak ona göre listelenme yapılacak
        key = gonderilecekListe[0][0]
        print("Gösterilen key'in oranı :" + str(gonderilecekListe[0][1]))

    else:
        key = "Null"

    return answers.get(key, '')


"""
Kullanıcıya cevap göndermeden önce listenin içinde döndürülen cevapların ortalamsının 
altında olan ve aynı olan verilerin diziden çıkarılması ve son listenin geri gönderilmesi 
"""


def gonder(liste, ortalama):
    yeniListe = []
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if float(liste[i][j][1]) > float(ortalama):
                yeniListe.append(liste[i][j])

    yeniListe = sorted(yeniListe, reverse=True)  # listeyi büyükten küçüge doğru sıralar

    for i in range(len(yeniListe)):
        if i + 1 < len(yeniListe):
            if yeniListe[i][0] == yeniListe[i + 1][0]:
                yeniListe.remove(yeniListe[i])

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
