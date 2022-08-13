# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:48:26 2022

@author: User
"""


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni=0
    def __init__(self,ism,familiya,passport,tyil,ish_joy,malumot):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__ish_joy = ish_joy
        self.__malumot  = malumot
        Shaxs.__odamlar_soni+=1   
        
        
    @classmethod  
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni

        
    def get_ish_joy(self):
        return self.__ish_joy
    
    def get_malumot(self):
        return self.__malumot
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
 
       return yil - self.tyil
   
    def set_ish_joy(self, yangi_ish):
        """Ish joyini o'zgartirish"""
        self.__ish_joy = yangi_ish
        
inson = Shaxs("Hasan","Alimov","FB001122",1995,"maktab",'oliy')
inson = Shaxs("Husan","Alimov","FB001155",1995,"maktab",'orta')
inson = Shaxs("Ali","Olimov","FB001120",1998,"maktab",'oliy')
inson = Shaxs("Akbar","Salimov","FB005567",1985,"univer",'oliy')
print(f"{inson.get_info()}. {inson.get_age(2021)} {inson.get_ish_joy ()} {inson.get_yoshda.")    








