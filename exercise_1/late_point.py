#Comprehensions



#List Comprehensiom

salaries=[1000,2000,3000,4000,5000]
null_list=[]
def new_salary(salary):
    return int(salary*20/100+salary)

for salary in salaries:
    null_list.append(new_salary(salary))


for salary in salaries:
    if salary >3000:
        null_list.append(new_salary(salary))

    else:
        null_list.append(new_salary(salary*2))

a=[new_salary(salary*2) if salary<3000 else new_salary(salary) for salary in salaries]
print(a)

a=[salary *2 for salary in salaries]
print(a)
#Çok önemli eğer tek başına bir tane if varsa en sola yazılır
#fakat else ile kullanılacaksa bu sola yazılması gerekir !

a=[salary *2  for salary in salaries if salary<3000]
print(a)

a=[salary *2 if salary<3000 else salary*0  for salary in salaries ]
print(a)

b=[new_salary(salary*2) if salary<3000 else new_salary(salary*0.2) for salary
in salaries]
print(b)

stundents=["John","Mark","Venessa","Mariam"]
stundents_no=["John","Venessa"]


test_x=[stundent.lower() if stundent not in stundents_no else stundent.upper()  for stundent in stundents]
print(test_x)

#Dict Comprehension

dictonary={'a':1,
           'b':2,
           'c':3,
           'd':4}

dictonary.keys()
dictonary.values()
dictonary.items()
a={k:v**2 for (k,v) in dictonary.items()}
a={k.upper() :v for (k,v) in dictonary.items()}
a={k.upper() :v**2 for (k,v) in dictonary.items()}
print(a.items())

