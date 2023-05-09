# car0 = {'model': 'lamborghini Aventador LB834',
#         'price': '420.000',
#         'year': 2011,
#         'colour': 'yellow',
#         'km': 3000
        
#         }
# car1 = {'model': 'Bugatti Chiron',
#         'price': '3.000.000',
#         'year': 2018,
#         'colour': 'blue',
#         'km': 25
#         }
# car2 = {'model': 'Ferrari SF90 Spider',
#         'price': '57.000',
#         'year': 2020,
#         'colour': 'red',
#         'km': 2500
#         }
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['colour']} colour, "
#       f"and it's price is {car['price']}$. "
      
#       )
# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['colour']} colour, "
#       f"and it's price is {car['price']}$. "
      
#       )
# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['colour']} colour, "
#       f"and it's price is {car['price']}$. "
      
#       )#too long right? simpler version is below.Using nesting.

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"The model of the car is {car['model'].title()}, "
#           f"it is in {car['colour']} colour, "
#           f"and its price is {car['price']}$ "
#           )
                                        #Method dictionaries using for var in:

                                            


# malibus = []
# for n in range(10):
#     new_car = {'model': 'malibu',
#                'colour': None, # unknown colour
#                'year': 2020,
#                'price': None,
#                'korobka': 'mexanika'
#         }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['colour'] = 'Black'

# for malibu in malibus[3:6]:
#     malibu['colour'] = 'Red'   
# for malibu in malibus[6:10]:
#     malibu['colour']= 'Blue'
# for malibu in malibus[3:6]:
#     malibu['korobka'] = 'avtomat'
# for malibu in malibus:
#     if malibu['korobka'] == 'avtomat':
#         malibu['price'] = '35000$'
#     else:
#         malibu['price'] = '28000$'
       
# for malibu in malibus:
#     print(malibu)

# dasturchilar = {'Ali': ['html, ', 'css.'],
#                 'Vali': ['c++,', 'javascript.'],
#                 'G\'ani': ['bootstrap, ', 'scalp.'],
#                 'Shahzod': ['Java, ', 'Python.']
#                 }
# for dasturchi, tillar in dasturchilar.items():
#     print(f"\n{dasturchi} quyidagi dasturlash tillarini biladi! ")
#     for til in tillar:
#         print(f"{til.upper()}")

# for dasturchi, tillar in dasturchilar.items():
#     print(f"\n{dasturchi} quyidagi dasturlash tillarini biladi!: ", end ='')
#     for til in tillar:
#         print(f"{til.upper()}", end = '')

# colleagues = {
#     'ali': {'familiya': 'valiev',
#             'tugulgan yil': 2002,
#             'malumot': 'oliy',
#             'tillari': ['php,' , ' bootstrap.']
#             },
#     'vali': {'familiya': 'aliev',
#              'tugulgan yil': 2000,
#              'malumot': 'orta mahsus',
#              'tillari': ['html,' , ' css.']
#              },
#     'hasan': {'familiya': 'bokijonov',
#               'tugulgan yil': 2003,
#               'malumot': 'oliy talim',
#               'tillari': ['html',',css,', 'javascript.']
#               }
#               }

# for ism, info in colleagues.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tugulgan yil']}-yilda tu'gulgan. "
#           f"\nMa'lumoti: {info['malumot'].title()}."
#           "\nQuyidagi dasturlash tillarini biladi! "
#           )
#     for til in info['tillari']:
#         print(f"{til.upper()}", end = '')


                                           #Practical exercises:
                                               #ex1-2
# billionaire_0 = {'name': 'Andrew Tate',
#                'year': 1986,
#                'car': 'Bugatti Chiron',
#                 'net worth': '350.000.000$'
#                 }
# billionaire_1 = {'name': 'Ilon Musk',
#                  'year': 1971,
#                  'car': 'Mclaren f1',
#                  'net worth': '172.000.000.000$'
#                  }
# billionaire_2 = {'name': 'Jeff Bezos',
#                  'year': 1964,
#                  'car': 'Honda Accord',
#                  'net worth': '126.000.000$'
#                  }

# billionaires = [billionaire_0, billionaire_1, billionaire_2]
# for billionaire in billionaires:
#     print(f"\n{billionaire['name']} was born in {billionaire['year']}."
#           f"\nHe owns many cars. One of his loved cars is {billionaire['car']} "
#           f"and his net worth is {billionaire['net worth']}."
#           )
                                           #Exercise №3
# movies = {'Jaloliddin': ['Shousheng redemption', 'Interstellar', 'World War Z'],
#            'Shohruh': ['Peaky Blinders', 'Avatar', 'Matrix'],
#            'Shaxzod': ['Spiderman', 'Batman', 'Super-man']
#            }
# for name, movies in movies.items():
#     print(f"\n{name.title()}'s favourite films are: ")
#     for film in movies:
#         print(film)




                                         #ex3
# countries = {'Uzbekistan': {'capital': 'Tashkent',
#                             'population': '32.000.000',
#                             'currency': 'som',
#                             'language': 'Uzbek'
#                             },  
#              'Poland': {'capital': 'Warsaw',
#                         'population': '35.000.000',
#                         'currency': 'zlot',
#                         'language': 'Polish'},
#              'USA': {'capital': 'Washington D.C',
#                      'population': '329.000.000',
#                      'currency': 'dollar',
#                      'language': 'English'
#                  }
#               }
# for country, info in countries.items():
#     print(f"\nThe capital of {country} is {info['capital']}, "
#           f"It's population consists of {info['population']} people. "
#           f"{info['currency'].title()} is an official currency of {country}"
#           f" and {info['language']} is their official language!"
#           )




                                 #ex 4
# countries = {'Uzbekistan': {'capital': 'Tashkent',
#                             'population': '32.000.000',
#                             'currency': 'som',
#                             'language': 'Uzbek'
#                             },  
#              'Poland': {'capital': 'Warsaw',
#                         'population': '35.000.000',
#                         'currency': 'zlot',
#                         'language': 'Polish'},
#              'USA': {'capital': 'Washington D.C',
#                      'population': '329.000.000',
#                      'currency': 'dollar',
#                      'language': 'English'
#                  }
#               }
# user = input("User, please input the name of the country! ").title()
# if user in countries:
#     info = countries[user]
#     print(    f"\nThe capital of {user} is {info['capital']}, "
#           f"It's population consists of {info['population']} people. "
#           f"{info['currency'].title()} is an official currency of {user}"
#           f" and {info['language']} is their official language!"
#           )
# else:
#     print("We do not have such country in our system")