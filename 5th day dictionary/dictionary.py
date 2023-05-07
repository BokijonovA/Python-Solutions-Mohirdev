                                       #Working with dictionaries

# en_uz = {'apple':'olma',
#          'pear': 'nok',
#          'grape': 'uzum',
#          'banana': 'banan',
#          'watermelon': 'tarvuz'
#          }
# print(f"Bizning uyda {en_uz['apple']}, {en_uz['grape']} va {en_uz['banana']} bor  ")



# mevalar = {'apple': 10000,
#            'pear': 13000,
#            'banana': 8000
    
#     }
# print(f"Olmaning narhi {mevalar['apple']} so'm")


                               #Adding new keys and values
# talaba = {'ism': 'Moturidiy',
#           'tugilgan_yil': 870,
#           'tugilgan_shahar': 'Samarqand'
    
#     }

# talaba['malumot'] = 'fiqh'
# talaba['fakultet'] = 4
# print(f" Bu talabamizni ismlari {talaba['ism']}, tugilgan yillari {talaba['tugilgan_yil']} va {talaba['tugilgan_shahar']} shahrida tugilganlar. ")


# talaba = {}
# talaba['ism'] = 'Asliddin Bokijonov'
# talaba['yosh'] = 20
# talaba['kurs'] = 2

# print(talaba['ism'])

                                         #method
# telefonlar = {'Ali': 'Iphone x',
#               'Vali': 'Samsung 22 Ultra',
#               'Zuhra': 'Iphone 9',
#               'Valeria': 'Iphone 12'
#     }

# phone = telefonlar.get('Ali', 'Bunday ism mavjud emas')
# print(f"{phone}")


                                     #Practical exercises

                                      #1
# ukam = {'ism': 'Muhammad Bokijonov,',
#         'yosh': 18,
#         'ish': 'Logistiks company'
#         }

# print(f"My brother's name is {ukam['ism']} he is {ukam['yosh']} years old and he works in {ukam['ish']} in Tashkent. ")
                                       #2
# taomlar = {'father': 'national plov',
#          'mother': 'chuchvara',
#          'brother': 'shashlik',
#          'sister': 'teramissio'
    
#          }

# print(f"My mammy's lovely food is {taomlar['mother']}")

 
                                   #3
# python = {'integer': 'is a whole number ',
#           'float': 'is a number with a deciminal point',
#           'string': 'is a sequence of numbers ',
#           'boolean': 'is a system of a logical thought that uses True/False statements',
#           'methon_get': ' is a method that derives specific key from the dictionary ',
#           'list': 'is a collection which is ordered and changeable',
#           'var': 'is a переменная',
#           'dictionary': 'is a data structure that stores key-value pairs! ',
#           'append': 'is a method which adds a value to the end of the text',
#           'title': ' is a method which capitalizes first letters of each word on a text',
#         }

# kalit = input("Foydalanuvchi kalit so'z kiriting! ").lower()
# print(python.get(kalit, 'Bunday kalit soz mavjud emas '))
                            #Below code is the same with the code above but with the if method.
# kalit = input("Foydalanuvchi kalit so'z kiriting! ").lower()
# if kalit in python:
#     print(f"{kalit} is {python.get(kalit)}")
# else:
#     print("Bunday kalit so'zi mavjud emas! ")

