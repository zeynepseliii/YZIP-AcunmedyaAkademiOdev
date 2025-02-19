from human import Human
import matematik as math

math.bol(20,2)


faiz = 1.59
vade = "36"
krediAdi = "ihtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

# vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
# print(type(vade))
# vade = vade + 12

#kullanıcıdan alınan input default olarak string consol da 

# string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print (f"seçtiğiniz vade sonucu ortaya çıkan vade {vade}")

# isim = input("isminizi giriniz")
metin = "merhaba {name}".format(name=123)
print(metin)

# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)

#listeler
#döngüler 
#fonksiyonlar

dizi = ["ihtiyaç kredisi","10",5,10.2,True]
print(dizi)

krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
print(krediler[2])
#eleman saymaya 1 den index saymaya 0 dan başlanır.

#.append fonksiyonu içerisine aldığı değeri gidip listenin son elemanına ekler.
krediler.append("özel kredi")
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0) #dizideki verdiğin indexe göre indexi siler. index vermezsen en sondakini siler
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)
krediler.remove("taşıt kredisi") #index sırasına göre bulduğu ilk elemanı siler
print(krediler)

krediler.extend(["y kredisi", "z kredisi"]) #birden fazla değeri tek satırda ekleme
print(krediler)

#for
# i=0 i<10

for i in range(10): #10 dahil değil, 0 dan başlar
    print("xx")
    print(i)

print("********************")

for i in range(5,10):
    print(i)

print("********************")    

for i in range(0,51,10):
    print(i)

print("********************")

# for i in range(0.1,0.5): -----> int bir değer olmalı
# print(i)

krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
for kredi in krediler:
    print(kredi)

print("*******************")

for i in range(len(krediler)):
    print(krediler[i])

print("*******************")

#sonsuz döngü

# i = 0
# while i < 10:
#     print("x")
#     i += 1
# print("y")

while True:
     print("x")
     break

print("***** son döngü *****")

i = 0
while i < len(krediler):
    print(i)
    i+=1
    print(krediler[i])
    if krediler[i] == "konut kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20

#definition define -----> fonksiyon tanımlanırken kullanılır.
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

# geri dönüş tipi olan fonksiyonlar

def calculateAndReturn(fiyat,indirim): #kullanılan fonksiyon isimleri tekrar kullanılabilir
    return fiyat-indirim # geriye her türlü veri dönebilir örneğin ["1","2"]

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

#void -----> geriye değer döndürmeyen
def calculatePrice(price, discount):
    print(price-discount)                          # fonk1

def calculatePriceAndReturn(price, discount):
    return price-discount                          # fonk2

print("********************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"159.Satır:  {fonk1}")
print(f"160.Satır:  {fonk2 + 100}")
print(fonk2)
print("********************")

#sınıflar -----> classlar
#modules
#paket yönetimi 

#self ----> this / tanımlanan nesnenin kendisi / bir class içinde fonksiyon kullanıyorsak self kullanmamız gerek (adı self olmak zorunda değil yaygın olarak kullanılıyor örn humanObj)
#classımın içindeki diğer alanlara erişebilmeyi sağlıyor

#instance => örnek 
#nesnelere erişebilmek için bir örnek (instance) oluşturmamız gerek

human1 = Human("Halit")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Cem")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("merhaba")

