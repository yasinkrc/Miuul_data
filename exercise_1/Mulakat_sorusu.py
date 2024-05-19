
#Amaç :Çift sayıların karesi alınarak bir sözlüğe eklenmke istemektedir
#Key'ler orijinal değerler value'lar ise değiştirilmiş değerler

numbers=range(1,11)
new_dict={}

for n in numbers:
    if n%2==0:
        new_dict[n]=n**2


b={n:n**2 for n in numbers if n%2==0 }
print(b)

#Bir veri setindeki Değişken isimmleirni değiştirmek

['total','spending','alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']

import seaborn as sns

df=sns.load_dataset("car_crashes")

for col in df.columns:
    print(col.upper())
A=[]
for col in df.columns:
        A.append(col.upper())

df.columns=A
X=[col.upper() for col in df.columns]
print(X)


#İsminde "INS" olan değişkenlerin başına FLAG  diğerleirine NO_FLAG eklemek istiyoruz


A=["FLAG"+col if "INS" in col else "NO_FLAG"+col  for col in df.columns]
print(A)

"""  ***************************"""
print("  ***************************")

import seaborn as sns
import pandas as pd

df = sns.load_dataset("car_crashes")

num_cols = [col for col in df.columns if df[col].dtype != "O"]  # "O" yerine "object" kullanılabilir
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = {col: agg_list for col in num_cols}

print("****************")
print(df[num_cols].agg(new_dict))

#new

