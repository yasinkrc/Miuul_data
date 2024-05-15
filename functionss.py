
print("Yasin")
help(print)

def naber():
    """
    naber yasin
    :return:
    """
def calculate(x):
    print(x+2)


calculate(2)

help(naber())

def selam()-> int:
   return 5

print(selam())

help(naber())

list_store=[]

def add_element(a,b):
    c=a*b
    list_store.append(c)
    print(list_store)

add_element(5,6)
add_element(66,8)
add_element(66,4)

def belediye(  x, y ,z) ->float :

    a=(x*y)/z
    return a

print(belediye(1,6,8))
print(belediye(1,6,54))
print(belediye(1,545,3.66))

def hesapla(a,b,c) ->tuple:

    a=a*2
    b=b*2
    c=c*2
    d=(a*b)/2
    return a,b,c,d


print(hesapla(1,56,7))
print(type(hesapla(1,56,7)))