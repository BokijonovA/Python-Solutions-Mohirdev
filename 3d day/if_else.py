# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:16:26 2023

@author: Asliddin
"""

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())       
    
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())

# user = input("Foydalanuvchi ismingizni kiriting! ")
# user = user.lower()
# if user == "admin":
#     print("Xush kelibsiz admin. Foydalanuvchilar ro'yhatini korasizmi")
# else:
#     print(f"Xush kellibsiz {user.title()}!")

# son1 = int(input("Foydalanuvchi 1chi sonni kiriting"))
# son2 = int(input("Foydalanuvchi 2chi sonni kiriting"))
# if son1 == son2:
#     print("Ushbu ikki son teng")
# else:
#     print("Ushbu sonlar bir biriga teng emas!")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

# son = int(input("Foydalanuvchi istalgan soningizni kiriting! "))
# if son >= 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.

# son = int(input("Foydalanuvchi son kiriting! "))
# if son >= 1:
#     print(son**0.5)
# else:
#     print("Musbat son kiriting!")


#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# sonlar = int(input("Foydalanuvchi juft son kiriting! "))
# for juft_son in range(0,1000,2):
#     if sonlar == juft_son:
#         print("Rahmat")
# for toq_son in range(1,1000,2):
#     if sonlar == toq_son:
#         print("Foydalanuvchi juft son kiriting!")
 
#2 second variant to solve the problem

# sonlar = int(input("Foydalanuvchi juft son kiriting! "))
# if sonlar % 2:
#     print("Foydalanuvchi juft son kiriting")
# else:
#     print("Raxmat")

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# user_yosh = int(input("Foydalanuvchi yoshingizni kiriting! "))
# if user_yosh <= 4 or user_yosh >=60:
#     print("Foydalanuvchi sizga tekin")
# elif user_yosh <=18:
#     print("Foydalanuvchi sizga 10000 som boladi")
# elif user_yosh >= 19 and user_yosh <= 59:
#     print("Foydalanuchi sizga 20000 ming som boladi")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# son1 = int(input("Foydalanuvchi 1chi sonni kiriting! "))
# son2 = int(input("Foydalanuvchi 2chi sonni kiriting! "))

# if son1 == son2:
#     print("ikkala son bir biriga teng!")
# elif son1>= son2:
#     print("Birinchi son ikkinchi sondan katta")
# else:
#     print("Ikkinchi son birinchi sondan katta")

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["nok", "piyoz", "olma", "ziemniaki", "pecharki", "yog", "shakar", "pomidor", "ananas", "uzum"]
# yangi_savat = []
# yangi_savat_soni = int(input("Mahsulotlar sonini kiriting(minimum 5 ta): "))
# if yangi_savat_soni >= 5:
#     for son in range(yangi_savat_soni):
#         product = input(f"{son + 1}chi mahsulotni kiriting!")
#         yangi_savat.append(product)
#     for mahsulot in yangi_savat:
#         if mahsulot in mahsulotlar:
#             print(f"Bu mahsulot, ya'ni {mahsulot} bizda bor")
#         else:
#             print(f"Bu mahsulot, ya'ni {mahsulot} bizda yoq")
# else:
#       print("Iltimos kamida 5 ta mahsulot kiriting")      
        






# mahsulotlar = ["nok", "piyoz", "olma", "ziemniaki", "pecharki", "yog", "shakar", "pomidor", "ananas", "uzum"]
# savat = []

# is_working = True
# while is_working:
#     savat_soni = int(input("Mahsulotlarni sonini kiriting(mimimum 5 ta!): "))
#     if savat_soni >= 5:
#         for son in range(savat_soni):
#             n = input(f"{son + 1}chi mahsulotni kiriting! ")
#             savat.append(n)
#         for mahsulot in savat:
#             if mahsulot in mahsulotlar:
#                 print(f"Bu mahsulot, ya'ni {mahsulot} bizni do'konda bor")
#             else:
#                 print(f"Bu mahsulotm ya'ni {mahsulot } bizni do'konda yo'q")
#         is_working = False
#     else:
#         print("Kallenga sani! Minimum 5 ta dedimku")
#         is_working = True
    


# mahsulotlar = ["nok", "piyoz", "olma", "ziemniaki", "pecharki", "yog'", "shakar", "pomidor", "ananas", "uzum"]
# yangi_savat = []
# savat_soni = int(input("Hurmatli, klient! Nechta mahsulot oldingiz? "))
# if savat_soni >= 5:
#     for son in range(savat_soni):
#         produkt = input(f"{son +1}chi mahsulotingizni nomini kiriting! ")
#         yangi_savat.append(produkt)
#     for mahsulot in yangi_savat:
#         if mahsulot in mahsulotlar:
#             print(f"Hurmatli klient, ushbu {mahsulot} do'konimizda bor.")
#         else:
#             print(f"Hurmatli klient, ushbu {mahsulot} do'konimizda yoq")
# else:
#     print("Hurmatli klient, 5 ta yoki 5 tadan ko'p mahsulotni kiriting!")
# mahsulotlar = ['manti', 'somsa', 'qazi', 'kotlet', 'nuggets', 'hamburger', 'cheeseburger', 'wiesmac', 'mcroyal', 'veggi' ]
# savat = []
# savat_soni = int(input("Foydalanuvchi nechta mahsulot oldingiz? "))
# if savat_soni >= 5:
#     for son in range(savat_soni):
#         produkt = input(f"Foydaluvchi {son + 1}chi mahsulotingizni nomini kiriting!")
#         savat.append(produkt)
#     for taom in savat:
#         if taom in mahsulotlar:
#             print(f"Foydalanuvchi ushbu {taom} bizning dokonda bor ")
#         else:
#             print(f"Foydalanuchi ushbu {taom} bizning do'konda yo'q ")
# else:
#     print("Foydalanuvchi 5ta yoki 5 tadan ko'p mahsulot kiriting")
    

# mahsulotlar = ['manti', 'somsa', 'baliq', 'shorva', 'kotlet', 'nuggets', 'hamburger', 'cheeseburger', 'wiesmac', 'mcroyal', 'veggi' ]
# savat = []
# print("Foydalanuvchi 5 ta mahsulotni ni nomini kiriting! ")
# if savat_soni == 5:
#     for son in range(savat_soni):
#         product = input(f" Foydalanuvchi {son + 1} chi mahsulotingizni nomini kiriting! ")
#         savat.append(product)
# for taom in mahsulotlar:
#     if savat in mahsulotlar:
#         print("Bizda hamma mahsulotlar mavjud")
#     for taom in savat:
#             if taom not in mahsulotlar:
#                 print(f"Bizda ushbu {taom} mavjud emas")
                

# mahsulotlar = ['manti', 'somsa', 'baliq', 'shorva', 'kotlet', 'nuggets', 'hamburger', 'cheeseburger', 'wiesmac', 'mcroyal', 'veggi' ]
# savat = []
# for n in range(5):
#     savat.append(input(f"Foydalanuvchi {n+1}chi zakazingizni kiriting "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f" Dok'onimizda quyidagi mahsulotlar yo'q")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz soragan barcha mahsulotlar dokonimizda mavjud ")
        
# mahsulotlar = ['manti', 'somsa', 'baliq', 'shorva', 'kotlet', 'nuggets', 'hamburger', 'cheeseburger', 'wiesmac', 'mcroyal', 'veggi' ]
# savat = []
# for n in range(5):
#     savat.append(input(f"Foydalanuvchi {n + 1}chi zakazingizni kiriting! "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f"Do'konimizda ushbu mahsulotlar yo'q")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Do'konimizda barcha mahsulotlar mavjud")

# foydalanuvchilar = ['Pantera', 'Toxic blade', 'Panda', 'Ninja', 'Orbit']
# user = input(f" Foydalanuvchi loginingizni kiriting! ")
# if user in foydalanuvchilar:
#     print(f"Login band yangi loginni kiriting! ")
# else:
#     print("Hush kelibsiz foydalanuvchi! ")
# son = int(input("Foydalanuvchi biror bir butut son kiriting! "))
# for n in range(2, 11):
#     if not(son % n): 
#         print(f" {son} soni {n}ga qoldiqsiz bo'linadi! ")
    














    
    
























