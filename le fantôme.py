import random
import time
while True:
    hayat=True
    score=0
    print ("Üç tane kapı ile karşılaştın. Karşında bir not buldun.")
    time.sleep(2)
    print ("Notta 'Karşında 3 tane kapı durmakta.")
    time.sleep(2)
    print ("Kapıların birinde çok aç bir tane hayalet saklanmakta.")
    time.sleep(2)
    print ("Eğer onun olduğu kapıyı seçersen hayalet seni yutacak.")
    time.sleep(2)
    print ("Eğer onun olduğu kapıyı seçmezsen 1 puan kazanacaksın.'")
    time.sleep(2)
    while hayat:
        hayalet=random.randint(1,3)
        porte=int(input("1. kapıyı mı, 2. kapıyı mı, 3. kapıyı mı açmak istersin? "))
        if porte==hayalet :
            hayat=False
            time.sleep(1)
            print("Olamaz hayalet ile karşılaştın! Kaybettin!")
        else :
            score=score+1
            time.sleep(1)
            print ("Bravo!")
            time.sleep(1)
            print ("3 tane yeni kapı ile karşılaştın.")
            print ("---------------------------------------------------------------------------------------------------------------")
    print ("Puanınız : ", score)
    print("---------------------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------------")
    time.sleep(5)