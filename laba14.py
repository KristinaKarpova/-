n = int(input())
if n == 0:
    print(n)
elif n < 0:
    print("Число должно быть положительным")
elif n > 0:
    two_in_power = 2
    power = 1
    while two_in_power <= n:
        two_in_power *= 2
        power += 1
    print(power)
