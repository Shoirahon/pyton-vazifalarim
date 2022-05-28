# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:00:35 2022

@author: User
"""
py_izohli_lugati={
    'value':'lugatdagi qiymatni chiqarish',
    'sorted':'alfavit bn chiqarish',
    'items':'kalit va qiymat juftliklari chiqadi',
    'boolean':'mantiqiy qiymat',
    'float':'o\'lik son',
    'integer':'butun son',
    'string':'matn',
    'input':'foydalanuvchidan ma\lumot qabul qilish',
    'if':'shartlarni tekshirish operatori',
    'for':'biror amalni qayta-qayta bajarish sikli'
   }

for kalit, qiymat in sorted(py_izohli_lugati.items()):
    print(f"{kalit.title()} - {qiymat}")
    
    
    
    
dav_poytahti={
    'o\'zb':'toshkent',
    'rossiya':'moskva',
    'xitoy':'pekin',
    'italiya':'rim',
    'aqsh':'washinton',
    'korea':'seul',
    'kirgizistron':'bishkek',
    }
    
print('dav_poytahtlari:')
for davlat in sorted(dav_poytahti):
    print(davlat.upper())
    
print('dav_poytahtlari:')
for davlat in sorted(dav_poytahti.values()):
    print(davlat.title())
    
    
mamlakat= input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
poytahti= dav_poytahti.get(mamlakat, 'Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
print(poytahti)
    
    
menu={
      'salat':10000,
      'osh':20000,
      'manti':16000,
      'choy':4000,
      'mastava':15000,
      'shashlik':25000,
     }    
    
print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
