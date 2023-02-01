while True :
    kilo = float(input("Kilonuzu kg olarak giriniz : "))
    boy = float(input("Boyunuzu metre olarak giriniz : "))
    vki = kilo/boy**2
    if vki > 30 and vki <= 40 :
        print ("Obezsin")

    elif vki > 40 and vki <= 50 :
        print ("Morbid obezsin")

    elif vki > 50 :
        print ("SUPER obezsin")

    elif vki <= 30 and vki >= 25 :
        print ("Fazla kilolusun")

    elif vki < 25 and vki >= 18.5 :
        print ("Kilon normal")

    elif vki < 18.5 and vki >= 12 :
        print ("Zayifsin")

    elif vki < 12 :
        print ("Asiri zayifsin")