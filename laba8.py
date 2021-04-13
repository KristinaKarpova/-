s = str(input())
ls = s.split(" ")
a = int(ls[0])
c = str(ls[1])
b = int(ls[2])
if c == "+":
    rez = a + b;
    print(rez)
elif c == "-":
    rez = a - b;
    print(rez)
elif c == "*":
    rez = a * b;
    print(rez)
elif c == "/":
    rez = a / b;
    print(rez)
else:
    print("Введена некорректная операция")
