# -*- coding: utf-8 -*-
"""
Created on 27.09.2019 20:10

@author: Erdem Şahin - Merve Gülaçtı- Furkan Berk Aktaş
"""

from KiyaslamaAlg import KiyaslamaAlgoritamalari
import noisy_text_normalization
import json

questions = ["Danışman ne iş yapar?",
             "Kayıt için ne yapmam gerekiyor ?",
             "gelemiyorum kayıt için ne yapmam gerekiyor",
             "kayıt için gerekli evraklarım eksik kayıt yaptıra bilir miyim", "afdhgjafgda",
             "Askerlik tecil nasıl yapılır?"]

i = 0
for x in questions:
    print(i, " :", x)
    i = i + 1

# json = json.dumps(SıkSorulanSorularData.faq)
# f = open("./JsonData/FaqData.json","w")
# f.write(json).encode('utf8')
# f.close()



f = open("JsonData/FaqData.json", "r", encoding="utf8")
data = f.read()
FaqData = json.loads(data)
f.close()

f = open("JsonData/AnswersData.json", "r", encoding="utf8")
data = f.read()
AnswersData = json.loads(data)
f.close()

<<<<<<< Updated upstream
=======
f = open("JsonData/JsonData.json", "r", encoding="utf8")
data = f.read()
JsonData = json.loads(data)
f.close()

>>>>>>> Stashed changes
# def gelen (questions):
#      OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(FaqData, AnswersData, questions)
#      return OrtakCevap


Soru = input("\nSoruyu Seçiniz : ")

questions1 = questions[int(Soru)]
question = noisy_text_normalization.Normalize(questions1)


# capitalize gelen cümlenin sadece baş harfinin büyük olmasını sağlar.
<<<<<<< Updated upstream
OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(FaqData, AnswersData, questions[int(Soru)].capitalize())
=======
OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(question).lower())
>>>>>>> Stashed changes

print("Bot:\n\t " + OrtakCevap)

# questions = input("Sorunuzu Giriniz : ")
# Cevap = KiyaslamaAlgoritamalari.possibleAnswer(faq, answers, questions)
# print("\nSoru : " + questions + "\n\n" + "Cevap : " + Cevap)
