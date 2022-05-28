# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:58:20 2022

@author: User
"""


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for avto in cars: 
    print(avto.title()) 


for avto in cars: 
    if avto == 'gm':
        print(avto.upper()) 
    else: 
        print(avto.title()) 
        
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']        
for avto in cars: 
    if avto != 'gm':
        print(avto.title()) 
    else: 
        print(avto.upper()) 
               
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")
 

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting:"))
if a==b: print(f"Sonlar teng: {a}={b}") 


son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")


son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')
      