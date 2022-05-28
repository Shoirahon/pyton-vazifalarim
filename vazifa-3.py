# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:38:36 2022

@author: User
"""
mevalar = ['olma','anor','uzum','gilos','banan','shaftoli']
mevalar.sort()
print(mevalar)
print(sorted(mevalar, reverse=True))

sonlar = [3,996,8,5,89,34] # range yordamida ketma-ket sonlar
print(sonlar)

# nouns = [1,2,3,4,5,6,7,8,9,10]    
nouns = list(range(1,11))
nouns.sort()
print(nouns)
nouns.sort(reverse=True)
print(nouns)

nouns.reverse()
print(nouns)



toq_sonlar = list(range(5,27,2))
print(toq_sonlar)
arzon=min(toq_sonlar)
print(arzon)
qimmat=max(toq_sonlar)
print(qimmat)
yigindi=sum(toq_sonlar)
print(yigindi)

# To'g'ri javoob
juft_sonlar = list(range(6, 27, 2))

a=max(juft_sonlar)
b=min(juft_sonlar)
print(a-b)


juft_sonlar=list(range(18,82))
print(juft_sonlar)

toq_sonlar=list(range(19,82,2))
print(toq_sonlar)
sonlar=toq_sonlar[0:10]
print(sonlar)

sonlar=juft_sonlar[18:28]
print(sonlar)

sonlar=juft_sonlar[22:]
print(sonlar)

mahsulotlar=['anor','olma','uzum','banan']
print(mahsulotlar)
mahsulotlar.append('sabzi')
print(mahsulotlar)

mahsulotlar.append('piyoz')
print(mahsulotlar)

mahsulotlar.append('chesnok')
print(mahsulotlar)

mevalar=mahsulotlar[0:3]
print(mevalar)

poliz_ekinlari=mahsulotlar[4:]
print(poliz_ekinlari)

mahsulot=('anor','olma','uzum','angir','dolana','sliva')
print(mahsulot)
# mahsulot[1]='gilos'
# print(mahsulot)

mahsulot = list(mahsulot)
mahsulot[1]='gilos'
print(mahsulot)

mahsulot = tuple(mahsulot)


















