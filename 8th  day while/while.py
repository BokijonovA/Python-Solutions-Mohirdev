name = input("Hello! What is your name? ")
question = f"Hello {name}! How old are you?"
yosh = input(question)
                                 while
son  = 1
while son <= 5:
    print(son, end = ' ' )
    son = son + 1
print("Dastur tugadi! ")



                                  while and input
print("Kiritilgan sonning kvadratinin qaytaruvchi dastur!")
user = "User, in order to know the square of the number, input number!"
user += "(In order to stop calculating please type 'exit'):\n"
answer = ''
while answer != 'exit':   
    answer = input(user)
    if answer != 'exit':
        print(float(answer)**2)
print("The program is shut down ")
                             

                                 boolean
print("Kiritilgan sonning kvadratinin qaytaruvchi dastur!")
user = "User, in order to know the square of the number, input number!"
user += "(In order to stop calculating please type 'exit'):\n"
sign = True
while sign:  
    answer = input(user)
    if answer == 'exit':
        sign = False
    else:
        print(float(answer)**2)
print("The program is shut down ")                 

                
                                break operator
print("Kiritilgan sonning kvadratinin qaytaruvchi dastur!")
user = "User, in order to know the square of the number, input number!"
user += "(In order to stop calculating please type 'exit'):\n"
while True:
    answer = input(user)
    if answer == 'exit':
        break
    else:
        print(float(answer)**2)
print('The program is shut down')
                              ex 2
sonlar = list(range(1,  10)) 
for son in sonlar:
    if son ==5:
        break
    print(f"{son}ning kvadrati {son**2}ga teng!")


                              continue operator
sonlar = list(range(1, 10))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son}ning kvadrati {son**2}ga teng")
                               
                                continue while

son = 0
while son < 10:
    son += 1
    if son %2 == 0:
        continue
    else:
        print(son)
                                    abadiy tsikl mistake
son = 0
while son < 10:
    if son %2 != 0:
        continue
    else:
        print(son)

                                     ex2 
son = 1
while son >0:
    son += 1
    if son %2 != 0:
        continue
    else:
        print(son)
                                      Practical exercises
user = "Please input your favourite books! "
user += "Please type 'exit' after finishing \n"
while True:
    books = input(user)
    if books == 'stop':
        break 
print('The program is shut down')


                                      ex2
savol = "Please input your age!"
while True:
    answer = input(savol)
    if answer == 'exit' or answer == 'quit':
        break
    yosh = int(answer)
    if yosh <= 7:
        narh = 2000
    elif yosh >= 7 and yosh <= 18:
        narh = 3000
    elif yosh >= 65:
        narh = 0
    if narh == 0:
        print("Foydalanuvchi sizga bepul")
    else:
        print(f"Foydalanuvchi sizdan {narh} ming so'm boldi")
        
                                        3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat =='exit':
        break
    elif float(qiymat) <0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print('Dastur tugadi')







