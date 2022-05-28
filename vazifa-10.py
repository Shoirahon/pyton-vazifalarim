# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:03:19 2022

@author: User
"""


# kitob="yoqtirgan kitobingizni kiriting"
# kitob+="(dasturni to'xtatish uchun 'stop' deb yozing): "
# daftar=''
# while daftar != 'stop':
#     daftar = input(kitob)
#     if daftar != 'stop':
#         print(daftar)
       
        
        
# yoshing = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(yoshing)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")
    

yoshing = "Yoshingizni kiriting:"

ishora = True
while ishora:
    qiymat = input(yoshing)
    if qiymat == 'exit' or qiymat == 'quit':
        ishora=False
    else:
        yosh = int(qiymat)
    
        if yosh<7:
            narh = 2000
        elif 7<=yosh<18:
            narh = 3000
        elif 18<=yosh<65:
            narh = 10000
        else: narh = 0
        
        if narh==0:
            print("Sizga chipta bepul")
        else:
            print(f"Chipta {narh} so'm")
    
while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif int(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    



