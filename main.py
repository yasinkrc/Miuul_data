

name="Merhaba"
type(name)

#Liste

list=["btc","eth","xrp"]
print(list)

# Sözlük --> Dictionaray
# Key --> value

dict_word={"name":"yasin","surname":"karaca","age":22,"isMarried":True}
print(dict_word)

for index , word in dict_word.items():
    print(index,":",word)

#Tuple

tup ="python","ml",11,True

for (i) in  enumerate(tup):
    print(i)

print(dir(int))
print("**************")
print(dir(str))


#Demet -- Tuple
# list'ten farkı elemalnarı değişmez


""" Set """

# - Değiştirilebillir

# - Sırasız ve Eşsizdir

# -Kapsayıcıdır

# -Kümeler gibi düşün

set1=set([1,2,3])
set2=set([1,3,5,4])


print(set1.difference(set2))
print(set1.symmetric_difference(set2)) #Kesişim bulunur
print(set1.intersection(set2))

print(set1-set2)
print(set2-set1)
print(set2&set1)
print(set1.union(set2))
print("*************************")
print(set1+set2)
print("*************************")
print(set1+set2)
print("*************************")


print(set1.isdisjoint(set2))
print(set1.issubset(set2)) #alt küeme
print(set1.issuperset(set2)) #birbirlerini kapsıyorlar mı ?


