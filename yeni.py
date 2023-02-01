import random
import time
    
Siniflistesi = ["Ali","Veli","Ayse","Safiye","Lale","Jale","Ekrem","Ismail","Aysegul","Emine","Zeynep","Etem"]
print ("8-A sinifina hosgeldiniz! Sinif listemiz : ", Siniflistesi)
time.sleep(4)
print ("Her islemden sonra sinif listesi gozukecektir")
while True :

    a = input("Sinifa yeni bir ogrenci eklemek icin A,\nsinif listesini alfabetik sekilde duzeltmek icin B,\nsinif listesini tamamen karistirmak icin C,\nsiniftan ismini yazdiginiz kisiyi cikartmak icin D,\nsiniftan hergangi birini secmek icin E,\nsinifta kac kisi oldugunu ogrenmek icin F,\nyazdiginiz ismin sinif listesinde kacinci oldugunu ogrenlmek icin G'ye tiklayiniz : " )
    if a == "A" or a == "a" :
        NouvelEleve = input("Sinifa eklenecek kisinin ismini giriniz: ")
        Siniflistesi.append(NouvelEleve)
        print ("Sinifa hosgeldin",NouvelEleve , "!")
        time.sleep(3)
    
    elif a == "B" or a == "b" :
        Siniflistesi.sort()

    elif a == "C" or a == "c" : 
        random.shuffle (Siniflistesi)

    elif a == "D" or a == "d" :
        isim = input("isim girin: ")
        time.sleep(2)
        for i in range (0, len(Siniflistesi)) :
            if isim == Siniflistesi[i] :
                x = Siniflistesi.pop(i)
                time.sleep(2)
                break

    elif a == "E" or a == "e" :
        s = random.choice(Siniflistesi)
        print (s, "secildi.")
        time.sleep(2)

    elif a == "F" or a == "f" :
        kackisi = len(Siniflistesi)
        print ("Sinifta", kackisi, "kisi bulunmakta")
        time.sleep(2)

    elif a == "G" or a == "g" :
        Isim = input("isim girin : ")
        for i in range (0, len(Siniflistesi)) :
            if Isim == Siniflistesi[i] :
                print (str(i+1) + ".", Isim)
                time.sleep(2)
                break


    else : 
        print ("Lutfen tekrar deneyiniz.")
        time.sleep(2)

    for i in range(0, len(Siniflistesi)):
        print(str(i+1) + '.', Siniflistesi[i])
        time.sleep(0.5)
    time.sleep(3)