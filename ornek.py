import csv
import os

with open("seferler.txt", "r") as f:
    kom_listesi = [line.strip() for line in f]

# Grafi oluşturma
graf = {}
for kom in kom_listesi:
    baslangic, _, hedef = kom.partition(" -> ")
    if baslangic not in graf:
        graf[baslangic] = []
    graf[baslangic].append(hedef)

# Komşuluk listesinin içeriğini listeleme
print("Komşuluk listesi:")
for sehir in graf:
    print(sehir + " -> " + " -> ".join(graf[sehir]))

# Giriş ve çıkış derecesi hesaplama
plaka = input("Plaka giriniz: ")
giris_derecesi = 0
cikis_derecesi = 0
for sehir in graf:
    if sehir.split("/")[1] == plaka:
        cikis_derecesi = len(graf[sehir])
    for komsu in graf[sehir]:
        if komsu.split("/")[1] == plaka:
            giris_derecesi += 1
            break
print(plaka + " plakalı şehrin giriş derecesi: " + str(giris_derecesi))
print(plaka + " plakalı şehrin çıkış derecesi: " + str(cikis_derecesi))

# Toplam kenar sayısının hesaplanması
kenar_sayisi = sum([len(graf[sehir]) for sehir in graf])
print("Toplam kenar sayısı: " + str(kenar_sayisi))

# Plakadan hangi şehirlere gidildiğinin bulunması
plaka = input("Plaka giriniz: ")
gidilecekler = []
for sehir in graf:
    if sehir.split("/")[1] == plaka:
        for komsu in graf[sehir]:
            gidilecekler.append(komsu)
print(plaka + " plakalı şehirden şu şehir düğümlerine gidilir: " + ", ".join(gidilecekler))

# Plakadan hangi şehirlere gelindiğinin bulunması
plaka = input("Plaka giriniz: ")
gelinilenler = []
for sehir in graf:
    for komsu in graf[sehir]:
        if komsu.split("/")[1] == plaka:
            gelinilenler.append(sehir)
print(plaka + " plakalı şehrine şu şehir düğümlerinden gelinir: " + ", ".join(gelinilenler))