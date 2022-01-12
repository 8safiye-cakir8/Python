import random
import time
taş=1
kağıt=2
makas=3
while True :
    bilgisayar=random.randint (1,3)
    bne=input("☺☻♥ ")
    if bilgisayar==1:
        print("bilgisayar taş yaptı")
        if bne=="taş":
            print("♥")
        elif bne=="makas":
            print("☺")
        elif bne=="kağıt":
            print("☻")
        else :
            print("Lütfen taş kağıt veya makas girirniz")
    elif bilgisayar==2:
        print("bilgisayar kağıt yaptı")
        if bne=="taş":
            print("☺")
        elif bne=="makas":
            print("☻")
        elif bne=="kağıt":
            print("♥")
        else :
            print("Lütfen taş kağıt veya makas girirniz")
    else :
        print("bilgisayar makas yaptı")
        if bne=="taş":
            print("☻")
        elif bne=="makas":
            print("♥")
        elif bne=="kağıt":
            print("☺")
        else :
            print("Lütfen taş kağıt veya makas girirniz")