print ("hosgeldiniz")
para=3000
while True:
    print("Su anki para miktariniz", para,"'dir")
    x= input("Hesabiniza para yuklemek icin 1, para cekmek icin 2'ye basiniz. Siz: ")
    if x=="1" :
        y=int(input("ne kadar para yuklemek istiyorsunuz? Siz: "))
        if y<=0 :
            print ("lutfen geçerli bir sayi giriniz.")
        elif y>10000 :
            print ("cok fazla para yukleyemezsiniz")    
        else :
            para=para+y
            print ("para yukleme isleminiz gerceklesmistir.")
    elif x=="2" :
        c= int(input("ne kadar para cekmek istiyorsunuz? Siz: "))
        if c>para :
            print ("Lutfen geçerli bir sayi giriniz.")
        elif c<=para :
            o= int(input("parayi nasil cekmek istiyorsunuz? nakit icin 3, kredi kartina eklemek icin 4'e basiniz. Siz: "))
            if o==3 :
                print ("para cekme isleminiz gerceklesmistir.")
                para=para-c
            elif o==4 :
                t=input("kredi karti sifrenizi giriniz. Siz: ")
                if t=="cakirlar" :
                    print ("para cekme isleminiz gerceklesmistir.")
                    para=para-c
                else :
                    print ("lutfen gecerli bir sifre giriniz.")
            else :
                print ("lutfen geçerli bir sayi giriniz.")
    else :
        print ("Lutfen geçerli bir sayi giriniz.")