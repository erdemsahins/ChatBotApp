# -*- coding: utf-8 -*-
"""
Created on 27.09.2019 20:10

@author: Erdem Şahin - Merve Gülaçtı- Furkan Berk Aktaş
"""

from KiyaslamaAlg import KiyaslamaAlgoritamalari
import json

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

# json = json.dumps(SıkSorulanSorularData.faq)
# f = open("./Data/FaqData.json","w")
# f.write(json).encode('utf8')
# f.close()


f = open("./Data/FaqData.json", "r")
data = f.read()
FaqData = json.loads(data)
f.close()

f = open("./Data/AnswersData.json", "r")
data = f.read()
AnswersData = json.loads(data)
f.close()

# def gelen (questions):
#      OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(FaqData, AnswersData, questions)
#      return OrtakCevap


Soru = input("\nSoruyu Seçiniz : ")
# capitalize gelen cümlenin sadece baş harfinin büyük olmasını sağlar.
OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(FaqData, AnswersData, questions[int(Soru)].capitalize())

print("Bot:\n\t " + OrtakCevap)

# questions = input("Sorunuzu Giriniz : ")
# Cevap = KiyaslamaAlgoritamalari.possibleAnswer(faq, answers, questions)
# print("\nSoru : " + questions + "\n\n" + "Cevap : " + Cevap)
