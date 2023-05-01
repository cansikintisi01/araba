import sys
import os
import random

if os.name == "nt":
    sil = "cls"
else:
    sil = "clear"

while True:
    print("Merhaba, araba satış listesi üzerinde hesaplama yapma programına hoş geldiniz.\nSizden 4 markadan 4 aylık bir satış fiyatı istenecek.\nSiz bu satış fiyatlarını girdikten sonra önünüze bir liste çıkacak.\nListede merak ettiğiniz soruların cevapları bulunmakta.\nBunlara listedeki soruların sıra sayısını yazarak ulaşabilirsiniz.\nHadi şimdi başlayalım.(Başlamak için Enter tuşuna basın.)")
    user_input = input()
    if user_input == "":
      os.system(sil)
      break
    else:
        print("Program sonlandırıldı.")
        sys.exit()
toplam = 0
b = 0
fiat = ["Fiat"]
print("Fiat için sayı giriniz: ")
for i in range(1, 5, 1):
  x = int(input())
  if x >= 0:
    fiat.insert(i, x)
  else:
    os.system(sil)
    print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
    sys.exit()

opel = ["Opel"]
print("Opel için sayı giriniz: ")
for i in range(1, 5, 1):
  x = int(input())
  if x >= 0:
    opel.insert(i, x)
  else:
    os.system(sil)
    print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
    sys.exit()

mercedes = ["Mercedes"]
print("Mercedes için sayı giriniz: ")
for i in range(1, 5, 1):
  x = int(input())
  if x >= 0:
    mercedes.insert(i, x)
  else:
    os.system(sil)
    print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
    sys.exit()

nissan = ["Nissan"]
print("Nissan için sayı giriniz: ")
for i in range(1, 5, 1):
  x = int(input())
  if x >= 0:
    nissan.insert(i, x)
  else:
    os.system(sil)
    print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
    sys.exit()
  
matrix = [
  ["Marka", "Ocak", "Şubat", "Mart", "Nisan"],
  fiat,
  opel,
  mercedes,
  nissan,
]
sayac = 0
while int(sayac) == 0:
  os.system(sil)
  print("{:<10}|{:^10}|{:^10}|{:^10}|{:^10}".format(*matrix[0]))
  print("-"*54)

  for i in range(1, len(matrix)):
    print("{:<10}|{:^10}|{:^10}|{:^10}|{:^10}".format(matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4]))

  print("\n1-En yüksek satışı yapan markaya gitmek için 1,")
  print("2-Her aydaki tüm markaların satış toplamlarını görmek için 2,")
  print("3-Bütün markaların toplam satış miktarını görmek için 3,")
  print("4-Her markanın en çok satışını gerçekleştirildiği ayı görmek için 4,")
  print("5-Her markanın en az satışını gerçekleştirildiği ayı görmek için 5,")
  print("6-En az satışı yapan markaya gitmek için 6,")
  print("7-Her aydaki en yüksek satışı yapan markaları görmek için 7,")
  print("8-Her aydaki en az satışı yapan markaları görmek için 8,")
  print("9-Listedeki herhangi bir sorunun cevabına gitmek için 9,")
  print("10-Listedeki satış fiyatlarını değiştirmek istiyorsanız 10,")
  print("11-Programı sonlandırmak isterseniz 11,")
  print("12-Yapımcı hakkında bilgi almak isterseniz 12 yazınız.")
  print("\n")
  b = int(input("Sayı Giriniz: "))
  if int(b) == 9:
    os.system(sil)
    rastgele = random.randint(1,8)
    secim = int(rastgele)
  else:
    secim = int(b)
  if int(secim) == 1:
    os.system(sil)
    x = []
    for i in range(1,5,1):
      x.append(matrix[i][1:5])
    y = max([max(row) for row in x])
    c = 0
    for i in range(len(x)):
      for j in range(len(x[i])):
        if x[i][j] == y:
          c += 1
    if c == 1:
      for i in range(1,5,1):
        if matrix[i][1:5].count(y) > 0:
          marka = matrix[i][0]
          ay = matrix[0][matrix[i][1:5].index(y)+1] 
          print("En yüksek satışı", marka, "markası", ay, "ayında yapmıştır.\nYaptığı satış fiyatı:",y)
          break
    else:
      print(
        "En fazla yapılan satışı buldum ama bu yapılan satışın sayısından birden fazla olduğu için hangisini kullanmam gerektiğini bilemedim. \nSayı:",
        y, "\nSayının kullanıldığı yerler aşağıda verilmiştir: ")
      for i in range(len(matrix)):
        for j in range(len(matrix[i])):
          if matrix[i][j] == y:
            marka = matrix[i][0]
            ay = matrix[0][j]
            print("Marka:", marka, "- Ay:", ay)
  elif int(secim) == 2:
    os.system(sil)
    x = [0, 0, 0, 0]
    for i in range(1, 5):
        for j in range(1, 5):
            x[j-1] += int(matrix[i][j]) 
    print(matrix[0][1], "ayında toplam:", x[0], "satış yapılmıştır.")
    print(matrix[0][2], "ayında toplam:", x[1], "satış yapılmıştır.")
    print(matrix[0][3], "ayında toplam:", x[2], "satış yapılmıştır.")
    print(matrix[0][4], "ayında toplam:", x[3], "satış yapılmıştır.")
  elif int(secim) == 3:
    os.system(sil)
    toplam = 0
    for i in range(1, 5):
        for j in range(1, 5):
            toplam += int(matrix[i][j])
    print("Bütün markaların toplam satış miktarı:", toplam)
  elif int(secim) == 4:
    os.system(sil)
    for i in range(1, 5):
        satismiktarlari = matrix[i][1:5]
        maxsatis = max(satismiktarlari)
        if maxsatis != 0:
            if satismiktarlari.count(maxsatis) > 1:
                marka = matrix[i][0]
                print(marka, "markasının en çok satışı aşağıdaki aylarda gerçekleşmiştir:")
                for ay_index in [j for j, k in enumerate(matrix[i][1:5]) if k == maxsatis]:
                    ay = matrix[0][ay_index+1]
                    print(ay, "ayında, satış miktarı:", maxsatis)
            else:
                marka = matrix[i][0]
                ay_index = matrix[i].index(maxsatis)
                ay = matrix[0][ay_index]
                print(marka, "markasının en çok satışı", ay, "ayında gerçekleşmiştir.\nSatış miktarı:", maxsatis)
  elif int(secim) == 5:
    os.system(sil)
    for i in range(1, 5):
        satismiktarlari = matrix[i][1:5]
        minsatis = min(satismiktarlari)
        if minsatis > -1:
            if satismiktarlari.count(minsatis) > 1:
                marka = matrix[i][0]
                print(marka, "markasının en az satışı aşağıdaki aylarda gerçekleşmiştir:")
                for ay_index in [j for j, k in enumerate(matrix[i][1:5]) if k == minsatis]:
                    ay = matrix[0][ay_index+1]
                    print(ay, "ayında, satış miktarı:", minsatis)
            else:
                marka = matrix[i][0]
                ay_index = matrix[i].index(minsatis)
                ay = matrix[0][ay_index]
                print(marka, "markasının en az satışı", ay, "ayında gerçekleşmiştir.\nSatış miktarı:", minsatis)
  elif int(secim) == 6:
    os.system(sil)
    x = []
    for i in range(1,5,1):
        x.append(matrix[i][1:5])
    y = min([min(row) for row in x])
    c = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == y:
                c += 1
    if c == 1:
        for i in range(1,5,1): 
            if matrix[i][1:5].count(y) > 0:
                marka = matrix[i][0]
                ay = matrix[0][matrix[i][1:5].index(y)+1] 
                print("En az satışı", marka, "markası", ay, "ayında yapmıştır.\nYaptığı satış fiyatı:",y)
                break
    else:
        print(
            "En az yapılan satışı buldum ama bu yapılan satışın sayısından birden fazla olduğu için hangisini kullanmam gerektiğini bilemedim. \nSayı:",
            y, "\nSayının kullanıldığı yerler aşağıda verilmiştir: ")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == y:
                    marka = matrix[i][0]
                    ay = matrix[0][j]
                    print("Marka:", marka, "- Ay:", ay)
  elif int(secim) == 7:
    os.system(sil)
    for ay_index in range(1, 5):
      satislar = [matrix[i][ay_index] for i in range(1, 5)]
      maxsatis = max(satislar)
      if maxsatis > -1:
        markalar = [matrix[i][0] for i in range(1, 5) if matrix[i][ay_index] == maxsatis]
        ay = matrix[0][ay_index]
        print(ay, "ayında en yüksek satışı yapan markalar:")
        if satislar.count(maxsatis) > 1:
            for marka in markalar:
                print(marka, "- Satış miktarı:", maxsatis)
        else:
            marka = markalar[0]
            print(marka, "- Satış miktarı:", maxsatis)
  elif int(secim) == 8:
    os.system(sil)
    for ay_index in range(1, 5):
      satislar = [matrix[i][ay_index] for i in range(1, 5)]
      minsatis = min(satislar)
      if minsatis > -1:
        markalar = [matrix[i][0] for i in range(1, 5) if matrix[i][ay_index] == minsatis]
        ay = matrix[0][ay_index]
        print(ay, "ayında en az satışı yapan markalar:")
        if satislar.count(minsatis) > 1:
            for marka in markalar:
                print(marka, "- Satış miktarı:", minsatis)
        else:
            marka = markalar[0]
            print(marka, "- Satış miktarı:", minsatis)
  elif int(secim) == 10:
    os.system(sil)
    print("Fiat için sayı giriniz: ")
    for i in range(1, 5, 1):
      x = int(input())
      if x >= 0:
        fiat.insert(i, x)
      else:
        os.system(sil)
        print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
        sys.exit()
    print("Opel için sayı giriniz: ")
    for i in range(1, 5, 1):
      x = int(input())
      if x >= 0:
        opel.insert(i, x)
      else:
        os.system(sil)
        print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
        sys.exit()
    print("Mercedes için sayı giriniz: ")
    for i in range(1, 5, 1):
      x = int(input())
      if x >= 0:
        mercedes.insert(i, x)
      else:
        os.system(sil)
        print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
        sys.exit()
    print("Nissan için sayı giriniz: ")
    for i in range(1, 5, 1):
      x = int(input())
      if x >= 0:
        nissan.insert(i, x)
      else:
        os.system(sil)
        print("Bir satışın 0'dan küçük olma ihtimali var mı?\nProgram ile dalga geçmeye çalıştığınız için Program Sonlandırıldı.")
        sys.exit()
  elif int(secim) == 11:
    os.system(sil)
    cevap = input("Programı sonlandırmak istiyor musunuz? (E/H): ")
    if cevap.lower() == "e" or cevap.lower() == "evet":
      sys.exit()
    elif cevap.lower() == "h" or cevap.lower() == "hayır":
      os.system(sil)
    else:
      print("Geçersiz cevap, lütfen 'e', 'evet' veya 'h'', hayır' yazınız.")
  elif int(secim) == 12:
    os.system(sil)
    print("Merhaba ben Carbonibon.\nSosyal medya adreslerimden beni takip edebilirsiniz.")
  else:
    os.system(sil)
    print("Lütfen listeden bir sayı seçip yazınız.")
  b = input("\nListeye geri dönmek için 0, programı sonlandırmak için herhangi bir tuşa basın: ")
  if int(b) != 0:
    os.system(sil)
    print("Program Sonlandırıldı.")
    sayac = 1
#Hocam 95 gelir mi :D