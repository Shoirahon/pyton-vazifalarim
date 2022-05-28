# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:01:02 2022

@author: User
"""


onam={"ism":"zamirahon","yosh":57,"t_yil":1965}
print(f"{onam['ism'].title()},{onam['yosh']}-yoshda,{onam['t_yil']}-yilda tugilgan")

taomlar = {
    'onam':'somsa',
    'ukam':'shirinliklar',
    'men':"mastava",
    'oglim':"osh",
    'qizim':"honim"
    }

taom = taomlar['men']
print(f"Mening sevimli taomim {taom}")

taom = taomlar['onam']
print(f"Onamning sevimli taomi {taom}")

taom = taomlar['qizim']
print(f"Qizimning sevimli taomi {taom}")


python_izohli_lugati = {
    'lower':"bosh harf",
    'if':"agar",
    'and':"va",
    'boolean':"true-false",
    'lugat':"key-value",
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
print(python_izohli_lugati['list'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    






