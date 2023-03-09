print("Hello World")
baslik = "Taşıt Kredisi"
print(baslik)

#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True | False 
yukselisteMi = False

# Matematiksel Operatörler

# +
print("---------------")
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# - 
print("---------------")
print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

# *
print("---------------")
print(5*5)
print(vade*12)
print(vade*ekVade)
print(36*6)

# /
print("---------------")
print(5/5)
print(vade/12)
print(vade/ekVade)
print(36/6)

print("---------------")
yeniVade = vade / 2 
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print("---------------")
print(10%2)
print(vade % 5)
print(vade % ekVade)

# Mantıksal (Karşılaştırma) Operatörler

print("---------------")
print(1 == 1)
print(1 == 2)
print("---------------")
print(1 > 2)
print(3 > 2)
print(1 > 1)
print(1 >= 1)
print("---------------")
print(1 < 2)
print(3 < 2)
print(1 <= 1)
print("---------------")
print( 1 != 1)
print( 1 != 2)
print("---------------")

# or, and
# or => Veya 
print(1 > 2 or 5 > 2)
# and => Ve
print(1 > 2 and 5 > 2)

print( 1 > 2 or 5 > 2 and 3 > 2 )
print (1 > 2 and 5 > 2 and 3 > 2)

# Karar Yapıları
# İf - Else Yapıları
sayi1 = 40
sayi2 = 20

#sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır

if sayi1 > sayi2:
    print("Sayi1 Daha büyüktür.")
else:
    print("Sayi2 Daha Büyüktür.")








