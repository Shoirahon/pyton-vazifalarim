# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:06:54 2022

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
        
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Shaxs: {self.ism} {self.familiya} {self.tyil}"
    
    def __eq__(self,y):
        """Tenglik"""
        return self.tyil == y.tyil
    
    def __lt__(self,y):
        """Kichik"""
        return self.tyil<y.tyil
    
    def __le__(self,y):
        """Kichik yoki teng"""
        return self.tyil<=y.tyil
     
inson = Shaxs("Hasan","Alimov","FB001122",1995,"maktab",'oliy')
inson1 = Shaxs("Husan","Alimov","FB001155",1998,"maktab",'orta')
print(inson)
print(inson1)
 

inson = Shaxs("Ali","Olimov","FB001120",1998,"maktab",'oliy')
inson = Shaxs("Akbar","Salimov","FB005567",1985,"univer",'oliy')     
        
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)

class Fan:
    """Fan klassi"""
    def __init__(self,name):
        self.name = name
        self.talabalar = []
    def __repr__(self):
            return f"{self.name} talabalari"
    
    def add_fanlar(self,talaba):
        if isinstance(talaba,Talaba): 
            self.fanlar.append(talaba)
        else:
            print("talaba obyketini kiriting")
        
    def __len__(self):
            return len(self.talabalar)
        
    def __getitem__(self,index):
            return self.talabalar[index]

        
fanlar = Fan("Fizika")
print(fanlar)

talaba1 = Talaba("Akbar Shukurillavev")
talaba2 = Talaba("Umar Alimov")
talaba3 = Talaba("Usmon Xalimov")
for Fan in [talaba1, talaba2, talaba3]:
salon1.add_avto(avto)



class Fan:
    """FAN klassi"""
    def __init__(self,name):
        self.name = name
        self.fanlar = []
    def __repr__(self):
        return f"{self.name} fanlari"
    def __len__(self):
        return len(self.fanlar)
    def __getitem__(self,index):
        return self.fanlar[index]
    def __setitem__(self,index,value):
        if isinstance(value,fan):
            self.fanlar[index]=value
    def add_fan(self,*qiymat):
        for fan in qiymat:
            if isinstance(fan,fanlar):
                self.fanlar.append(fan)
            else:
                print("Fan obyketini kiriting")

fan1 = Fan("Fizika")
fan2 = Fan("Ximiya"

fannomi1=fan("kuchlanish","atom massa","itarish kuchi")
fannomi2=fan("mendeleyev","atom massa","himik hossasi")
fannomi3=fan("","atom massa","itarish kuchi")






