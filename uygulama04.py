
metin="Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[0:20])

liste=["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)

sozluk={"Elma":"Ağaçta yetişen bir tür meyve", "Salatalık":"Fidan üzerinde büyüyen bir tür sebze"}

a=input("Kelime giriniz:")

if a =="Elma" :
    print("Ağaçta yetişen bir tür meyve")

if a == "Salatalık":
    print("Fidan üzerinde büyüyen bir tür sebze")
else:
    print("tekrar deneyiniz")

