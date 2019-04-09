__author__="Ayşe Yeliz"
sorular= ['Türkiyenin başkenti neresidir?',
          'Serenad kitabının yazarı kimdir ?',
          'Sarı ve mavi rengini karıştırırsak hangi renk ortaya çıkar ?',
          'Eyfel kulesi nerededir?',
          'İnsanlar ka yaşında oy kullanabilirler?',]
cevaplar =['A','C','B','C','E']
cevaplarA=['Ankara','Kemal Tahir','Siyah','İtalya', '15']
cevaplarB=['İstanbul','Yaşar Kemal','Yeşil','Prag','15']
cevaplarC=['Adana','Zülfü Livaneli','Kırmızı','Fransa','16']
cevaplarD=['İzmir','Orhan Kemal','Turuncu','Almanya','17']
cevaplarE=['Bursa','Halide Edip Adıvar','Mor','Malta','18']
puan=0
for i in range(len(sorular)):
    print("soru "+str(i+1)+":"+ sorular[i])
    print("A)"+cevaplarA[i])
    print("B)"+cevaplarB[i])
    print("C)"+cevaplarC[i])
    print("D)" +cevaplarD[i])
    print("E)" +cevaplarE[i])
    cevap=input("Cevabınızı giriniz: ")
if(cevaplar[i])==cevap.upper():
    puan+= 1
    print("Testiniz bitmiştir.Puanınız:" + str(int((puan/len(sorular))*100)))
