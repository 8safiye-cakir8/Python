while True :
    sayi=int(input("sayinizi giriniz : "))

    s=1
    if sayi >0 :
        for a in range (2, sayi) :
            if (sayi %a) ==0 :
                 s=2
                 break
    if s==2 :
        print (sayi, "asal sayi degil.")
    else :
        print (sayi, "asal sayidir.")