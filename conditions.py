1==1

if True :
    print("Selam")
else:
    print("Merhaba")


student = ["John","selam","ahd"]

for student in student:
    """print(student.upper(),end=",")"""
    print(student)


def new_salary(salary,rate):
    return int(salary*rate/100+salary)


new_salary(1500,10)
new_salary(2000,20)


salaries=[1000,1500,2000,2600,3000,35000,3554]

for salary in salaries :
    if salary>3000:
        print(new_salary(salary, 10)," ")
    else:
        print(new_salary(salary, 20)," ")



# Amaç : Aşağıdaki şekilde string değiştiren fonskiyon yazmak istiyoruz

#before: "hi my name is john and i am learning python"

text_string = "hi my name is john and i am learning python"
text_string="Merhaba beb yasin Nasılsın İYİMİSİN ?"

for (i, t) in enumerate(text_string):
    if(i%2==0):
        print(t.upper(),end="")
    else:
        print(t.lower(),end="")

print()
#Sabah kalkınca bu örneği fonksiyon yazarak yapmaya çalış


text_string="Miul Start Başla"
def func(str) :
    answer = ""
    for s in range(0, len(str)) :
        if (s%2==0):
            answer+=str[s].upper()
        else:
            answer+=str[s].lower()
    return answer


print(func("Merhaba Arkadaşlar"))

print()
#While

numer=1
while numer<5:
    print(numer)
    numer+=1


#Enumerate: Otomotik Counter / İndexer  le for loop

students=["John","Mark","Venessa","Mariam"]
A=[]
B=[]
for (i,d) in enumerate(students):
    if (i%2==0):
        A.append(d)
    else:
        B.append(d)
print(A)
print(B)


""" def tuple()->tuple:
    return  1,2,3,4

a,b,c,d=tuple()
print(a)
print(b)
print(c)
print(d) """

students=["John","Mark","Venessa","Mariam","Yasin"]

T=[]
C=[]
def divide_students():

    for (i,d) in enumerate(students):
        if(i%2==0):
            C.append(d)
        else:
            T.append(d)
    return [T,C]

print(divide_students())
index=[1,2,3,4,5]
students=["John","Mark","Venessa","Mariam","Yasin"]
Age=[10,11,12]

print(list(zip(index,students,Age)))

#***********************************************************

""" Lambda , Map , filter , reduce """

#lambda kullan at demek yani öyle kendini uyarla

new_sum= lambda a,b:a+b

new_sum(6,8)

#Map döngü yazmaktan bizleri kurtarır

salaries=[1000,2000,3000,4000]

def new_salary(x):
    return x*(0.2)+x
print(new_salary(1000))
print()
print()
for i in salaries:
    print(new_salary(i))

print(list(map(new_salary,salaries)))
print(list(map(lambda x:x*20/100+x,salaries)))
print(list(map(lambda x:x**2,salaries)))

#Filter --> çok az kullanılır
list_store=[1,2,3,4,4,5,6,4,4,5,46,1,321,9]
print(list(filter(lambda x:x%2==0,list_store)))


#Reduce  -- indirgemek demek

from functools import reduce

list_store=[1,2,3,4]
print(reduce(lambda a,b:a+b,list_store))