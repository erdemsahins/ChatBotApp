# -*- coding: utf-8 -*-
"""
Created on 27.09.2019 20:10

@author: Erdem Şahin - Merve Gülaçtı- Furkan Berk Aktaş
"""

import json

import noisy_text_normalization
from KiyaslamaAlg import KiyaslamaAlgoritamalari

questions = ["okul kantini nerede ?", "okul kantinine nasıl gidebilirim ?",
             "kantin mühendisliğin neresinde?", "mühendisliğe nasıl gidilir?", "Danışman ne iş yapar?",
             "Kayıt için ne yapmam gerekiyor ?",
             "gelemiyorum kayıt için ne yapmam gerekiyor",
             "kayıt için gerekli evraklarım eksik kayıt yaptıra bilir miyim", "afdhgjafgda",
             "Askerlik tecil nasıl yapılır?"]

i = 0
for x in questions:
    print(i, " :", x)
    i = i + 1



f = open("JsonData/JsonData.json", "r", encoding="utf8")
data = f.read()
JsonData = json.loads(data)
f.close()


Soru = input("\nSoruyu Seçiniz : ")

questions1 = questions[int(Soru)]
print(questions1)
print(questions)
question = noisy_text_normalization.Normalize(questions1)


# def gelen (questions):
#      OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(question).lower())
#      return OrtakCevap


# capitalize gelen cümlenin sadece baş harfinin büyük olmasını sağlar.
OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(question).lower())

print("Bot:\n\t " + OrtakCevap)

# questions = input("Sorunuzu Giriniz : ")
# Cevap = KiyaslamaAlgoritamalari.possibleAnswer(faq, answers, questions)
# print("\nSoru : " + questions + "\n\n" + "Cevap : " + Cevap)
