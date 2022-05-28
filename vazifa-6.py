# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:18:17 2022

@author: User
"""


a=int(input(f"juft son kiriting"))
if a>=0:
      print("rahmat")


yosh = int(input('Yoshingiz nechida? '))
if yosh<=4 or yosh>=60:
    price = 0
elif yosh<18:
    price = 10000
elif yosh>18:
    price = 20000
print(f"Sizga kirish {price} so'm" )

a=int(input(f"birinchi sonni kiriting"))
print(a)
b=int(input(f"ikkinchi sonni kiriting"))
print(b)
if a==b:
    print(f"{a}={b}")
elif a<b:
    print(f"{a}<{b}")
else:
    print(f"{a}>{b}")

mahsulotlar=['tuz','shakar','olma','guruch','banan','makaron','brinza','sir','grechka','sabzi']
savat=[]
for i in range(5):
    mahsulot=(input(f"mahsulot kiriting"))
    

