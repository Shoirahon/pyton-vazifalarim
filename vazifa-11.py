# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:41:21 2022

@author: User
"""


# buyurtma =[]
# while True:
#     mahsulot = input("buyurtma mahsulot buyuring:")
#     buyurtma.append(mahsulot)
#     javob = input("Yana buyurtma aytasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break
                 

# e_bozor = []
# while True:
#     mahsulot = f"mahsulot   nomini kiriting:"
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     e_bozor[mahsulot] = narh
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#      break
       
    
        
buyurtma=['anor','anjir','uzum','shaftoli']
mahsulot={
        'anor':20000,
        'anjir':10000,
        'uzum':50000,
        'shaftoli':80000
          }
while buyurtma:
    zakaz = buyurtma.pop()
    if zakaz in mahsulot.keys():
        narh = mahsulot[zakaz]
        print(f"{zakaz.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")