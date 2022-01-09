a=0
while True :
    print (a)
    x = input("s tusu sayiyi bir arttirir, c tusu sayiyi bir azaltir, t tusu sayiyi sifirlar: ")
    if x == "s" :
        a=a+1
    elif x == "c":
        a=a-1
    elif x == "t":
        a=0
    else :
        a=a