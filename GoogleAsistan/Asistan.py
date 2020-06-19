from gtts import gTTS
from playsound import playsound
import random
import os

#Burda bir dosya oluşturacağız ve bu dosya yer kaplamaması için silmemiz gerekiyor. Random ve os paketlerini dahil ediyoruz

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,1000)  #Dosya silinemediğinde bu random dosyalar aynı isimde olduğu için  çakışmasın istiyoruz
    file = './GoogleAsistan/audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
