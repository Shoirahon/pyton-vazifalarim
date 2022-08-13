# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:19:22 2022

@author: User
"""


class User:
    """User nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil,email):
        """Userning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.email = email
        
    def get_info(self):
        user1.get_info()
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil}. {self.email}. yilda tu'gilganman")
            
user1 = User("Akbarjon","Shukrillayev",2012,"ashukrillayevgmail722#gmail.@com")
user2 = User("Husan","Akbarov",2004,"hakbarovgmail455#gmail.@com")
user3 = User("Ali","Akbarov",2008,"aakbarovgmail766#gmail.@com")
      
print(user1.email)
