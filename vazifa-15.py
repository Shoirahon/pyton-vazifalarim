# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:20:06 2022

@author: User
"""
class Auto:
    """Auto nomli klass yaratamiz"""
    def __init__(self,model,rang,karobka,narh):
        """Autoning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.kilometr = 0

    def get_info(self):
        return f"{self.model} {self.rang}. {self.karobka}. {self.narh}. {self.kilometr} km yurgan."
    def set_kilometr(self,kilometr):
        """mashinaning yolini yangilovchi metod"""
        self.kilometr = kilometr
    def update_kilometr(self):
         """moshinani yurgan yoli 1taga ko'paytirish"""
         self.kilometr+= 1   

auto1 = Auto("lasetti","oq","avtomat",35000)
print(auto1.get_info())
   
auto1.update_kilometr() 
print(auto1.get_info())
        
        
class Autosalon():
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzili = manzil
        self.avtolar_soni = 0
        self.sotuvdagi_mashinalar = []
    def add_salon(self, avto):
        """Sotuvga mashina qo'shish"""
        self.sotuvdagi_mashinalar.append(avto)
        self.avtolar_soni += 1
        
    def get_name(self):

         """salon nomi"""
         return self.nomi
    def get_salon(self):
         """salondagi mashinalar  haqida ma'lumot"""
         return [x.get_info() for x in self.sotuvdagi_mashinalar]
    def get_salon_num(self):
         """salondagi mashinalar soni"""
         return self.avtolar_soni
   
salon1 = Autosalon('chigatoy', 'Boburshoh')
auto2 = Auto('captiva', 'qora', 'avtomat', 45000)
salon1.add_salon(auto1)
salon1.add_salon(auto2)
print(salon1.get_salon())
        
        
        