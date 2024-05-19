
z=8j+10
print(type(z))

text = "The goal is to turn data into information, and information into insight."

text=text.upper()
text=text.replace(".","").replace(",","")
text=text.split(" ")
print(text)

""" 
Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
"""
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

print(len(lst))
print(lst[0],lst[10])
new_lst=lst[:4]
print(lst)
lst.pop(8)
print(lst)
lst.append("Merhaba")
print(lst)
lst.insert(8,"N")
print(lst)
"""
Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz.
"""
dict = {'Christian': ["America", 18],
'Daisy': ["England", 12],
'Antonio' : ["Spain", 22],
'Dante': ["Italy", 25]}

print(dict.keys())
print(dict.values())

dict["Daisy"][1]=13
print(dict)

dict["Ahmet"]=["Turkey",24]
print(dict)

dict.pop("Antonio")
print(dict)


"""
Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız
"""
ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for (index ,ogrenci) in enumerate(ogrenciler,1):
    if index<=3:
        print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}")
    if index>=4:
        print(f"Tıp Fakültesi {index-3}. öğrenci: {ogrenci}")


"""
Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
Beklenen Çıktı:
Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu,
farklı ve ortak elemanlar için ise intersection ve difference metodlarını kullanınız.
"""


kume1 = set(["data", "python","Selam"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(kume1,kume2):
    if (kume2.issuperset(kume1))!=True:
        print(kume2.difference(kume1))
    else:
        print("Kumeler birbirini kapsiyor")

kume(kume1,kume2)

"""
Mühendislik Fakültesi 1 . öğrenci:Ali
Mühendislik Fakültesi 2 . öğrenci:Veli
Mühendislik Fakültesi 3 . öğrenci:Ayşe
Tıp Fakültesi 1 . öğrenci: Talat
Tıp Fakültesi 2 . öğrenci: Zeynep
Tıp Fakültesi 3 . öğrenci: Ece
"""