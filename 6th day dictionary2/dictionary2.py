                                      #items()

# talaba = {'ism': 'Alijon',
#           'fakultet': 'IT',
#           'yil': 2000,
#           'yosh': 23
#     }

# for key, values in talaba.items():
#     print(f"Keys: {key}")
#     print(f"Values: {values}\n")


# telefonlar = {'Asliddin': 'Poco F3 pro',
#               'Jaloliddin': 'Iphone 11',
#               'Humoyun': 'Poco X3 pro',
#               'Shaxzod': 'Iphone 11 pro'
    
#     }
# for key, value in telefonlar.items():
#     print(f"{key}ning telefoni {value}")

                                     #keys()

# mahsulotlar = {'apple': 5000,
#                'pear': 7000,
#                'plum': 9000,
#                'banana': 12000
    
#     }
# print("Do\'kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)

# bozorlik = ['apple', 'orange', 'apricot', 'banana', 'plum']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"Bu mahsulotning ya'ni {mahsulot}ning narhi {mahsulotlar[mahsulot]}so'm!")
# for product in bozorlik:
#     if product not in mahsulotlar:
#         print(f"Iltimos do'koningizga {product} ham olib keling")

                                          #values()
# telefonlar = {'Asliddin': 'Poco F3 pro',
#               'Jaloliddin': 'Iphone 11',
#               'Humoyun': 'Poco X3 pro',
#               'Shaxzod': 'Iphone 11 pro'
    
#     }
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar! ")
# for telefon in telefonlar.values():
#     print(telefon)
    
                                        #set() combines repetitive values as one.


# telefonlar = {'Asliddin': 'Poco F3 pro',
#               'Jaloliddin': 'Iphone 11',
#               'Humoyun': 'Poco X3 pro',
#               'Shaxzod': 'Iphone 11 pro',
#               'Shoxruh': 'Iphone 11 pro',
#               'Nodirbek': 'Iphone 11'
    
#     }
# for telefon in set(telefonlar.values()):
#     print(telefon)

                                    #class set
# toys = {'bear', 'ball', 'car', 'lamp', 'bear', 'car'}
# print(sorted(toys))


                                      # sorted
# mahsulotlar = {'apple': 5000,
#                'pear': 7000,
#                'plum': 9000,
#                'banana': 12000
    
#     }
# for mahsulot in sorted(mahsulotlar):
#     print(f"{mahsulot.title()}")
    
                                  #ex1

# python = {'Asliddin': 2,
#           'Shaxzod': 3,
#           'Jahongir': 4,
#           'Jalol': 1,
#           'Andrew': 4,
#           'Tristan': 2,
#           'Ilon': 1,
#           'Farida': 4,
#           'Hurshid': 3,
#           'Abdulaziz': 2
#     }

# for key, value in sorted(python.items()):
#     print(f"{key} {value} kursda oqiydi! ")
                                   #ex2

# davlatlar = {'Uzbekistan': 'Tashkent',
#              'Poland': 'Warszawa',
#              'South Korea': 'Seoul',
#              'North Korea': 'Pyongyang',
#              'Tajikistan': 'Dushanbe',
#              'Turkey': 'Ankara',
#              'Sri Lanka': 'Sri Jayawardenepura Kotte',
#              'France': 'Paris',
#              'Czech': 'Praga',
#              'Russia': 'Moskva',
#              'United States of America': 'Washington'
    
    
    
#     }
# for country, capital in sorted(davlatlar.items()):
#     print(f"{country.title()}'s capital is {capital}")
                                      #ex3
                                      
                                      
# davlatlar = {'Uzbekistan': 'Tashkent',
#              'Poland': 'Warszawa',
#              'South Korea': 'Seoul',
#              'North Korea': 'Pyongyang',
#              'Tajikistan': 'Dushanbe',
#              'Turkey': 'Ankara',
#              'Sri Lanka': 'Sri Jayawardenepura Kotte',
#              'France': 'Paris',
#              'Czech': 'Praga',
#              'Russia': 'Moskva',
#              'United States of America': 'Washington'
    
    
    
#     }
# user = input('If you want to know the capital of country please, input country\'s name! ').title()
# a = davlatlar.get(user, 'There is no such country in our system! ')
# if user in davlatlar:
#     print(f"{user}'s capital is {a}")
# else:
#     print(a)
                                        #4
# restaurant = {'shashlik': 30000,
#               'kapsalon': 56000,
#               'wiesmac': 23000,
#               'big mac': 30000,
#               'mcroyal': 20000,
#               'cheeseburger': 13000,
#               'hamburger': 10000,
#               'veggi burger': 50000,
#               'veggi wrap': 30000,
#               'osh': 30000   
#     }
# print("Honorable klient please order 3 kanapki from the restaurant! ")
# orders = []
# for n in range(3):
#     orders.append(input(f"{n+1}chi taomni kiriting! "))
# for order in orders:
#     if order in restaurant:
#         print(f"{order.title()}'s price is {restaurant[order]}")
#     else:
#         print(f"Sorry we do not serve {order}! ")










            
    
    
    