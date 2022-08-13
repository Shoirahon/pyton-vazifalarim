# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:33:26 2022

@author: User
"""
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
inson = Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")    

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
        
        
        
# talaba = Talaba("Valijon","Aliyev","FA112299",2000)
# print(talaba.get_info())        


# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.fan=[]
        
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def fanga_yozil(self, fan):
        """Talabaga fanni qo'shuvchi metod"""
        self.fanlar.append(fan)
        
    def remove_fan(self, fan):
        """Talabani fanini o'chiruvchi metod"""
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz.")
            
    # def get_fanlar(self):
    #     return fan.nomi for fan in self.fanlar
        
        
class Fan:
    """fan haqida malumot"""
    def __init__(self,nomi,oqituvchi):
        self.nomi = nomi
        self.oqituvchi = oqituvchi
        
    def get_fan(self):
        """fanlarni ko'rish"""
        return f"{self.nomi.title()} fani. O'qituvchi: {self.oqituvchi}."

matem = Fan('Matematika', 'Sanobar')
fizika = Fan('Fizika', 'Dildora')
ingliz = Fan("Ingliz tili", 'Sevara')

talaba = Talaba("Imomali", "azizov", 'ab223442', 2002, '0003045')

talaba.fanga_yozil(matem)
talaba.fanga_yozil(fizika)

talaba.remove_fan(ingliz)


























        
        
        
        
        
        
        