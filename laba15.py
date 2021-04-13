import random
comp = random.randrange(0, 100)
count = 1
while True:
    try:
        u_digit = input("Какое число? \n")
        u_digit = int(u_digit)
    except:
        print("Это не число")
    else:
        if u_digit < 0 or u_digit > 100:
            print("Введите число от 0 до 100")
        else:
            if u_digit < comp:
                print("Загаданное число больше")
            if u_digit > comp:
                print("Загаданное число меньше")
            if u_digit == comp:
                print("В яблочко!"); break
            count += 1
    if count > 5:
        print("Вы проиграли, было загадано", comp); break

