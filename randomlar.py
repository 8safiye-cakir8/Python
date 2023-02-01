import random
while True :
    liste = ['Jale','Veli','Ali','Ayşe','Ekrem','İsmail','Safiye']
    print('Listemiz ','Jale-','Veli-','Ali-','Ayşe-','Ekrem-','İsmail-','Safiye`dir')
    input("Random kişiyi seçmek için Enter'a basınız.")
    x=random.choice(liste)
    print (x)