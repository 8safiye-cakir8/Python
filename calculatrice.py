while True :
    x=int(input("lutfen ilk sayizi giriniz  "))
    y=int(input("lutfen ikinci sayinizi girinz  "))
    t=input("lutfen islemnizi giriniz toplama icin 1, çikarmak için 2, çarpmak için 3,bolmek icin 4, uslu sayilar icin 5'e basiniz :   ")
    # int kullanmama nedenimiz eger kullanici harf girerse hata vermesin diye
    if t=="1" :
        print (x,"+",y,"=",x+y)
    elif t=="2" :
        print (x,"-",y,"=",x-y)
    elif t=="3" :
        print (x,"x",y,"=",x*y)
    elif t=="4" :
        if x>y :
            print (x,":",y,"=",x/y,"| kalan: ",x%y)
        elif y>x :
            print (y,":",x,"=",y/x,"| kalan: ",y%x)
    elif t=="5" :
        print (x, "**", y, "=", x**y)
    else :
        print ("lutfen geçerli bir sayi giriniz.")
# *=carpma islemi icin
# /=bolme islemi icin
# **=uslu sayilar icin kullanilir
# %=bolme isleminin kalanini gosterir