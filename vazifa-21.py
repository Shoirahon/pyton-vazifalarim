# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:53:04 2022

@author: User
"""


# yil = input("Yilingizni kiriting: ")
# try:
#     yil = int(yil)
   
# except:
#     print("Iltimos butun son kiriting")
# else:
#      print(f"Siz {2022-yil} yoshdasiz")
#      print("Dastur Tugadi!")


# a=5
# b=12
# try:
#     a/(b-b)
# except ZeroDivisionError:
#     print("bu amalni bajarib  bo'lmaydi")
    
#     print("0 ga bo'lib bo'maydi")

# inson = {"ism":"Ali",
#         "yosh":"21",
#         "email":"ali@muhammad.com",
#         "phone":"998915259930"}

# key="familiya"
# try:
#     print(f'Foydalanuvchi: {inson[key]}')
    
# except KeyError:
#     print("Bunday kalit  so'z mavjud emas")
    
    
kitoblar = ['Yulduzli tunlar ','Mehrobdan chayon','Alvido qurol','Saodat asri qissalari','Otgan kunlar']
try:
    print(kitoblar[7])
except IndexError:
    print(f"Ro'yxatda {len(kitoblar)} ta kitobdan bo'shqa kitob qolmadi")    
    
    
    
    
    
    
    
    
    
    
    
    