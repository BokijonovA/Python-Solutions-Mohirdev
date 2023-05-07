# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:00:53 2023

@author: Asliddin
"""

# bozorlik = ["piyoz", "un",  "yog", "olma" ]
# mahsulot = bozorlik.pop(2)
# print(mahsulot)
# print(bozorlik)

# ismlar = ["Jalol", "Jahongir", "Sherzod"]
# print(f" Salom {ismlar[0]} bugun choyhonaga chiqamizmi? ")
# print(f" Salom {ismlar[1]} yaxshimisan?")
# print(f" Salom {ismlar[2]} Ishlar qaley?")

# MASHQ
# sonlar = [1, -2, 3, 1.3]
# answer = sonlar[1] + sonlar[3]
# print(answer)
# print(sonlar[0] + sonlar[2])

# t_shaxslar = ["Amir Temur", "Abu Ali Ibn Sino", "Khalid Ibn Valid"]
# z_shaxslar = ["Ilon Musk", "Bill Gates", "Andrew Tate"]
# t_shaxslar.pop(0)
# z_shaxslar.pop(1)
# print(f"Men tarixiy shaxslardans {t_shaxslar[1]} bilan, zamonaviy shaxslardan esa {z_shaxslar[1]} bilan suhbat qilishni istar edim")

# friends = []
# friends.append("Sherzod")
# friends.append("Jalol")
# friends.append("Jahongir")
# friends.append("Axmedov")
# friends.append("Muhammad Aziz")
# print(friends)
# friends.remove("Jalol")
# friends.pop(0)
# yangi_kelgan_mehmon = friends.pop(0)
# friends.append(yangi_kelgan_mehmon)
# print(friends)
#print(yangi_kelgan_mehmon)

 
# sonlar = list(range(1, 11))
# print(sonlar)

# cars = ["bmw", "mercedes", "volvo", "Audi", "general motors", "tesla"]
# #cars.sort(reverse = True)
# print(sorted(cars))

# toq_sonlar = list(range(1, 20, 2))
# max_son = max(toq_sonlar)
# print(max_son)

# toys = ("bus", "car", "bear")
# toys = list(toys)
# print(type(toys))

# davlatlar = ["America", "russia", "UAE", "Uzbekistan"]
# a = sorted(davlatlar, reverse = False) 
# # davlatlar_soni = len(davlatlar)
# # davlatlar.sort(reverse = True)
# # davlatlar = sorted(davlatlar)
# #print(sorted(davlatlar, reverse = False))
# print(davlatlar)

# sonlar = list(range(120, 1200, 2))
# # sonlar = min(sonlar) + max(sonlar)
# #sonlar = len(sonlar)
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])


# taomlar = ["kebab", "chuchvara", "osh", "shorva", "manti"]
# nonushta = taomlar[:]
# nonushta.remove("chuchvara")
# nonushta.remove("shorva")
# nonushta.remove("manti")
# nonushta.append("tuhum")
# nonushta.append("sasiska")
# print(f"{taomlar} and {nonushta}")

# nonushta = tuple(nonushta)
# print(nonushta)
# nonushta = list(nonushta)
# nonushta[0] = "Qaymoq va non"
# print(nonushta)