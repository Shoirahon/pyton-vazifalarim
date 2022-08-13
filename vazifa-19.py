# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:44:32 2022

@author: User
"""
import pickle

with open('atamalar.txt') as fayl:
    atamalar = fayl.read()
    print(atamalar)

with open('pi_million_digits.txt','r') as fayl:
    PI = fayl.read()

def tkun_aniqla(tkun, pi=PI):
    if tkun in pi:
        print("Tug'ilgan kuningiz pi soni ichida bor")
    else:
        print("Tug'ilgan kuningiz pi soni ichida yo'q")
    
tkun_aniqla("20031986")

PI = PI.rstrip()
PI = float(PI)

with open('pi_mln.dat', 'wb') as fayl:  
    pickle.dump(pimln, fayl)
