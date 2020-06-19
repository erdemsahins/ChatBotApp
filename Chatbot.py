# -*- coding: utf-8 -*-
"""
Created on 27.09.2019 20:10

@author: Erdem Şahin - Merve Gülaçtı- Furkan Berk Aktaş
"""

import json
import noisy_text_normalization
from KiyaslamaAlg import KiyaslamaAlgoritamalari
from GoogleAsistan import Asistan
import time


# Json veri tabanını açar ve geçici ön bellege alır
f = open("JsonData/JsonData.json", "r", encoding="utf8")
data = f.read()
JsonData = json.loads(data)
f.close()


# Flasktan gelen veriyi algoritmalara gönderir
def gelen (questions1):
    question = noisy_text_normalization.Normalize(questions1)
    OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(question).lower())
    return OrtakCevap


questions = ["okul kantini nerede ?", "okul kantinine nasıl gidebilirim ?",
             "kantin mühendisliğin neresinde?", "mühendisliğe nasıl gidilir?", "Danışman ne iş yapar?",
             "Kayıt için ne yapmam gerekiyor ?",
             "gelemiyorum kayıt için ne yapmam gerekiyor",
             "kayıt için gerekli evraklarım eksik kayıt yaptıra bilir miyim", "afdhgjafgda",
             "Askerlik tecil nasıl yapılır?","danışman kimdir?"]

i = 0
for x in questions:
    print(i, " :", x)
    i = i + 1


Soru = input("\nSoruyu Seçiniz : ")
questions1 = questions[int(Soru)]


# questions1 = input("\nSoruyu Giriniz : ")

#Normalizasyon yapar
question = noisy_text_normalization.Normalize(str(questions1))
baslangic= time.time()
print("Sorunuz: "+str(question))


# lower gelen cümlenin bütün harflerini küçültmesini sağlar.
OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(question).lower())

print("Bot:\n\t " + OrtakCevap)
Asistan.speak(OrtakCevap)

son = time.time()
sure = son-baslangic
print("\nCecaplama Süresi: "+ str(sure))



# # excel dosyası için hazırlanan test verileri toplu test için kullan
#
# testdata = ["YKS sınavı ile yerleştim. Ne yapmam gerekiyor kayıt için?",
#  "YKS sınavı ile kazandım. Kayıt için gelebilecek durumda değilim ne yapmalıyım? Kaydı posta ile yollayarak yapabilir miyim?",
#  "Kayıt için gereken belgelerimde eksikler var. Belgeler tamamlanmadan kayıt yaptırabilir miyim?",
#  "Yüksek Öğretim Kurumları Sınavı sonucu KLÜ’ye yerleştim. Yerleşmeme rağmen kaydı gerçekleştirememe durumu olur mu?",
#  "Danışman hoca kimdir? Ne yapar?",
#  "Kayıt dondurabilir miyim?",
#  "Öğrenim ücreti hangi dönemde ve nasıl ödenir?",
#  "Öğrenci harçlarını kim belirliyor?",
#  "Belirtilen süre zarfında öğrenciler okula kaydını yaptıramazsa ne olur?",
#  "Kesin kayıt için önceden arayıp bir işlem yapmam gerekiyor mu?",
#  "Dönem ortalamam 1.80’in altında olduğunda kaç kredi ders alabiliyorum?",
#  "Başka bir yükseköğretimde kaydım var. Kayıt olmak için diplomamın kopyası yeterli olur mu?",
#  "Üniversiteye yerleşmeye hak kazandım fakat liseyi henüz bitiremedim. Nasıl kayıt yaptırabilirim?",
#  "Üniversiteye yeni kayıtların ders alma işlemleri nasıl yapılır?",
#  "Üniversitenin programlarına ÖSYM yerleşiminden başka bir şekilde kayıt olunabilir mi?",
#  "Öğrenci belgemi nereden almalıyım?",
#  "Daha önce bir yükseköğretimde kayıtlı olduğumdan dolayı başarılı durumdaki derslerim muaf olabilir mi? Nasıl?",
#  "GANO ve YANO ne anlama gelir?",
#  "Öğrenci harcımı yatırdıktan sonra kaydımı dondurdum. Kayıt dondurduğum dönem öğrenci harcımı yatırmalı mıyım?",
#  "Talebe kaydını sildirmek istediğinde ne yapmalı?",
#  "Askerlik erteleme işlemleri nasıl yapılır?",
#  "İlk sınıf öğrencileri üstten ders alabilir mi?",
#  "Öğrenim süremden sayılır mı kayıt yaptırmadığım dönem?",
#  "Lise diplomam olmadan kayıt yaptırabilir miyim?",
#  "Üniversitenin yerleşkelerine nasıl ulaşabilirim?",
#  "Kırklareli’nin barınma olanakları nelerdir?",
#  "Ne zaman ve nasıl staj müracaatı yapılır? İşletmelerde hangi staj yapabilirim?",
#  "Bölümümle alakalı programları nereden öğrenebilirim?",
#  "Okula girerken veya imtihanlarda öğrenci belgem yanımda yoksa ne yapabilirim?",
#  "Öğrenci toplulukları nelerdir? Nasıl katılabilirim?",
#  ]
#
# testdata = ["Üniversite kaydı nasıl yapılır",
#     "Şehir dışına çıkmadan üniversite kayıt yapma",
#     "Eksik belge ile kayıt yapılır mı",
#     "Üniversite kayıdının iptal olması",
#     "Kayıt görevlisi hocalar",
#     "Kaydımı nasıl dondurabilirim",
#     "2. Öğretim ücretleri",
#     "katkı yapı ücreti nedir",
#     "telafi kayıtları",
#     "nasıl kayıt yapabilirim",
#     "not sınırının altında en fazla kaç kredilik ders alabilirim",
#     "üniversite geçişi yaparken diploma fotokopisi geçerli midir",
#     "liseden mezun olmadan kayıt olma",
#     "ders kaydı nasıl yapılır",
#     "YKS olmadan kayıt yapama",
#     "öğrenci belgesi nasıl alırım",
#     "muafiyet derslerimi öğrenme",
#     "YANO ve GANO nedir",
#     "kaydımı dondurduğumda öğrenim ücreti ödemeli miyim",
#     "askerli tecil etme",
#     "üstten ders alma",
#     "kayıt yaptırmadığım dönem öğrenim süremden sayılır mı",
#     "diplomasız kayıt yapma",
#     "kampüse nasıl giderim",
#     "erkek yurtları",
#     "staj başvurusu şartları",
#     "haftalık ders programı ve sınav takvimi",
#     "öğrenci kartım olmadan giriş yapabilir miyim",
#     "öğrenci klüpleri başvuru",
#     "okul mailim ne",
#     "okul maili şifresini sıfırlama",
#     "EBYS ye  giriş yapma",
#     "EBYS giriş yaptığım halde e-imza alamıyorum",
#     "EBYS paraf atamıyorum",
#     "OBS giriş yapamıyorum",
#     "Bilgi Yönetim Sistemi nedir",
#     "DTS nedir",
#     "İYS nedir",
#     "Personel sistemi nedir",
#     "BAP nedir",
#     "Proje yöneticisi olmanın şartları",
#     "Proje başvurusu şartları",
#     "En fazla kaç proje ile başvurusu yapabilirim",
#     "Proje başvurularının değerlenderilmesi",
#     "Proje destek parası",
#     "Proje süresi en fazla ne kadar",
#     "Proje başvurusunda başka kurumlarla anlaşma yapabilir miyim",
#     "Proje personeli ile ilgili uygulama prensibi",
#     "Diğer proje konsferanslarından BAP fonundan yararlanabilir miyim",
#     "Üniversitenin proje için desteği var mı",
#     "Sempozyum ücretleri",
#     "Proje malzemelerini nasıl alabilirim",
#     "Proje raporlarının teslimi",
#     "Proje bütçeleri arasında geçiş sağalabilir miyim",
#     "Proje için zamanım veya ek bütçem yetmedi ne yapmalıyım",
#     "Proje için maksimum süre",
#     "Projemin yayına dönüşme zorunluluğu var mı",
#     "Proje yayını için ne yapmalıyım",
#     "Diğer projeler için ne yapmalıyım",
#     "Araştırma görevlisi proje için istenen talepleri gerçekleştirebilir mi",
#     "Ek NAP projesi başvurusu yapma",
#     "NAP projesine ek tez çalışması alabilir miyim",
#     "Yapabileceğim en fazla tez araştırması",
#     "Çocuk üniversitesi nedir",
#     "Çocuk üniversitesi atölye tarihler",
#     "Çocuk üniversite atölye saatleri",
#     "Çocuk üniversitesinde en fazla kaç atölyeye katılabilirim",
#     "Çocuk üniversitesi başvuru",
#     "Çocuk üniversitesi ücreti",
#     "Çocuk üniversitesi ücretini nereye yatırılır",
#     "Çocuk üniversitesi eğitimleri nerde yapılır",
#     "Çocuk üniversitesi eğitim kadrosu",
#     "Çocuk üniversitesi ulaşım",
#     "Yeni mezun olanların katılabileceği programlar",
#     "E-kitapları katalog taramada görebilir miyim",
#     "Veri tabanı bilgilerini indirme",
#     "Veri tabanına okul dışından ulaşma",
#     "Kütüphane veri tabanları",
#     "Kütüphanede bulunmayan yayınlara nasıl ulaşırım",
#     "Başka bir kütüphaneden kitap getirtmek için ne yapmalıyım",
#     "Kütüphane hesabında ne gibi işlemler yapabilirim",
#     "Kütüphane hesabıma nasıl giriş sağları",
#     "Kitap uzatma işlemi nasıl yapılır",
#     "Ödünç kitap tarihi uzatma",
#     "Kütüphaneden en fazla kaç kitap ve en fazla kaç gün alabilirim",
#     "Kütüphane açık saatler",
#     "Microsoft IT Akademi nedir",
#     "Kırklareli IT Akademi nedir",
#     "Kırklareli IT Akademi eğitimleri",
#     "Kırklareli IT Akademi eğitimlerinin kazandırdıkları",
#     "Kırklareli IT Akademi tarihleri",
#     "Kırklareli IT Akademi kayıt şartları",
#     "Kırklareli IT Akademi kayıt",
#     "Kırklareli IT Akademi eğitim süreci",
#     "KLUZEM ortak dersler",
#     "Uzaktan eğitim gereksinimleri",
#     "KLUZEM nedir",
#     "KLUZEM şifremi unuttum",
#     "KLUZEM devam zorunluluğu",
#     "KLUZEM dersleri için sistem gereksinimleri",
#     "KLUZEM dersleri için hangi tarayıcıyı kullanmalıyım",
#     "KLUZEM dersi video ayarları yapma",
#     "Uzaktan eğitimde nasıl daha başarılı olurum",
#     "Erasmus şartları",
#     "Erasmus not sınırı zorunlu mu",
#     "Erasmus sınav notumu neler etkiler",
#     "Erasmus sınavları ve sınav ücretleri",
#     "Erasmusta ne kadar bütçe verilecek",
#     "Erasmus bütçe şartları",
#     "Erasmus bütçe değerlendirilmesi",
#     "Erasmus bütçe ödeme tarihleri"
#     "Erasmus konsolosluk ücreti neden ödeniyor",
#     "Neden Erasmus ücreti için 2 anlaşma yapıyoruz",
#     "Pasaport defter bedeli",
#     "Neden Erasmus Euro hesabı açmalıyım",
#     "Erasmus bütçe tarihlerinin belirlenmesi",
#     "Erasmus hiybe tarihleri",
#     "Erasmusta karşılama olacak mı",
#     "Erasmus bütçeleri yeterli olur mu",
#     "Erasmus derslerinin dili ne olacak",
#     "Erasmusta dil kursu olacak mı",
#     "Erasmus üniversiteleri",
#     "İntibak belgesi nasıl doldururum",
#     "Erasmus kabul mektubum gelmedi",
#     "Erasmus vize kabul olmadı ne yapmalıyım",
#     "Erasmus harcını nereye yatırmalıyım",
#     "Erasmus için ders kaydı yapma",
#     "Erasmus öğrenci beyannamesi nedir",
#     "İlk yılımda Erasmusa kayıt olabilir miyim",
#     "Ön lisans için öğrenci değişim",
#     "Erasmus yaptığım halde doktorada da yapabilir miyim",
#     "Erasmus üniversite kodları",
#     "Kalan Erasmus bütçesini nasıl alabilirim",
#     "Kalan Erasmus bütçesinin verilme şartları",
#     "Erasmustan erken döndüm ne yapmalıyım",
#     "Ders intibaklarının AKTS düzenlenmesi",
#     "Erasmus AKTS nin yurtiçinde dönüşümü nedir",
#     "Engelliler için Erasmus şartları",
#     "Erasmus sınavında yedekler ne yapmalı",
#     "Erasmus tercih değiştirme",
#     "Erasmus uzatma şartları",
#     "Erasmus bütçe anlaşmasında 1 dönemlik olmasına rağmen öğrenim anlaşması 2 dönemse ne yapmalıyım",
#     "Erasmus katılım şartları",
#     "Erasmus katılım şartları",
#     "OLS nedir",
#     "OLS sistemindeki diller",
#     "OLS katılım şartları",
#     "AB anketi nedir",
#     "Öğrenim harekliliği öncesinde hangi sigortaları yapmalıyım",
#     "Hiybe değerlendirme",
#     "Erasmus ve Ortak Ülkeler ülkeleri",
#     "Seyahat hiybesi alma",
#     "Ortak Ülkeler projesi aylık öğrenci bütçesi",
#     "OÜP çevrimiçi dil desteği",
#     "Okul içi kantin nerde"
#     ]

# for x in testdata:
#     OrtakCevap = KiyaslamaAlgoritamalari.AlgoritmaCagir(JsonData, str(x).lower())
#     print("Bot:\n\t " + OrtakCevap)