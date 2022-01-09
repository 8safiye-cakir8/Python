import random
import time

can = 15
ccan = 30
while can > 0 and ccan > 0:
    x = input("Saldırı için A, savunma için D: ")
    x = x.upper()
    a = random.randint(1, 2)
    if x == "A":
        if a == 1:
            print("Ataktayız, zarlar atılıyor...")
            time.sleep(2)
            zar = random.randint(1, 6)
            czar = random.randint(1, 6)
            if zar > czar:
                print("Canavara üstün geldin.")
                guc = zar - czar
                ccan = ccan - guc
                print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
                time.sleep(1)
            else:
                print("Canavar üstün geldi.")
                cguc = czar - zar
                can = can - cguc
                print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
                time.sleep(1)
        else:
            print("Atağı savuşturdu.")
            print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
            time.sleep(1)
    elif x == "D":
        if a == 1:
            print("Atak savuşturuldu.")
            print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
            time.sleep(1)
        else:
            print("Hiçbir şey olmadı, her iki taraf da defansta.")
            print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
            time.sleep(1)
    else:
            print("Geçersiz hamle!")
            print("""
Canavarın canı: {}
Bizim canımız: {}
""".format(ccan, can))
            time.sleep(0.5)

if ccan < 0:
    print("Canavarı mağlup ettin.")
    time.sleep(5)
elif can < 0:
    print("Canavar tarafından yenildin.")
    time.sleep(5)