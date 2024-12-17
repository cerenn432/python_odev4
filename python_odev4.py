# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def selamlama():
    for i in range(11):
        print("MERHABA")

selamlama()


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def dikdortgeninAlani(uzun_kenar, kisa_kenar):
    alan = float(uzun_kenar) * float(kisa_kenar)
    return alan

def dikdortgeninCevresi(uzun_kenar,kisa_kenar):
    cevre=(float(uzun_kenar)+float(kisa_kenar))*2
    return cevre

uzun_kenar = input("Uzun Kenar: ")
kisa_kenar = input("Kısa Kenar: ")

dikdortgeninAlani(uzun_kenar,kisa_kenar)
dikdortgeninCevresi(uzun_kenar, kisa_kenar)
print("Alan: ", dikdortgeninAlani(uzun_kenar,kisa_kenar))
print("Cevre: ", dikdortgeninCevresi(uzun_kenar, kisa_kenar))


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
import random
yazi_tura = random.randint(1,2)

if yazi_tura == 1:
  print("Yazı geldi.")
else:
  print("Tura geldi.")


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))
 
print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
 
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           print(sayi)


# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
sayi = 98
def tam_bolen(sayi):
    return [i for i in range(1, sayi + 1) if sayi % i == 0]
print(tam_bolen(sayi))