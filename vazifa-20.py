# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:32:57 2022

@author: User
"""
import json
import pickle

data = {
        "Model" : "Malibu",
        "Rang" : "Qora", 
        "Yil":2020, "Narh":40000
        }
data_json = json.dumps(data)
print(data_json)

talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba_json = json.loads(talaba_json)
print(talaba_json)


filename = 'data.json'
with open(filename, 'w') as d:
    data = d.write(data_json)
    print(type(data))


filename = 'talaba.json'
with open(filename, 'wb') as f:
    talaba = pickle.dump(talaba_json, f)
    print(type(talaba))

