from random import randint

can_sayisi=5
print("bir çiçek ismi\n")
kelimeler=["gül","menekşe","orkide","lale","nilüfer"]
secilen_kelime=kelimeler[randint(0,len(kelimeler)-1)]
bos=[]
for i in range(len(secilen_kelime)):
         bos.append("_")

print(bos)



while (can_sayisi>0):
       print("kalan canınız "+str(can_sayisi))
       girilen__harf=input("Bir harf giriniz.")
       if (girilen__harf in secilen_kelime):
           for l in range(len(secilen_kelime)):
                  if(girilen__harf==secilen_kelime[l]):
                      bos[l]=secilen_kelime[l]

           print(bos)
           if("_" not in bos):
                  print("Tebrikler!Bildiniz")
                  break

       else:

            can_sayisi =can_sayisi -1

if (can_sayisi==0):
        print("Canınız bitti.Oyunu Kaybettiniz.!!")



