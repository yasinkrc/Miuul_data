# We will study


"""

:type(int , float , str ....)
2**3=8
10/2 =5
10/3=3.33
10//3=3
number+=30


"""

a = 5
b = "Yasin"

print("Merhaba", a)
print("Merhaba", b)

print("Merhaba" + str(a))
print("Merhaba" + b)

name = "YASİN"
surname = "KARACA"

print("Merhaba benim adım {} soyadım {}'dır".format(name, surname))
result = 100 / 7
print(f"the result : {result:1.5f}".format(result))

x = name * 3
print(x)

# Pythonda String Metotlar

"""
upper lower  title capitalize strip split 
"""
str_ = "merhaba"

str_ = str_.center(50, '*')

print(str_)

name = "Selam merhaba ben Yasin."

# name = name[:-2]
# name=name[::2]
# name=name[::-1]
# name=name[::-1]
# print(name)

"""
sayi=4
print(type(sayi))





print(type(str(sayi)))
"""
""" 
string  = "Hello There . aaa  My name , aaa , aaa , bbb , aaab , bbb ,c is  Yasin "

result = string
result = string.upper()
result = string.lower()
result = string.capitalize()
result = string.title()
result = "Yasin" in string
result = "ysin" in string
result = string.strip('a').strip('b').strip('c')

result=string.split()
result="-".join(string)
result=string.count("aaa")
result=string.index("aaa")
print(result)


liste=[]

for i in range(0,3):
    for j in range(0,3):
        liste.append(j)



tuple=1,2,3,"selam" ,True

for i in tuple:
    pass

print(type(tuple))

x= {
    "NabizDegiskenligi": 165,
    "SpO2": 98,
    "CiltIletkenligi": {
        "ECGOlculumu": "Var",
        "StresSeviyesi": "Dusuk"
    }
 
"""