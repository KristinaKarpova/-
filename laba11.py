a, n, = int(input()), int(input())
def power(a, n):
    z, c, rez, arr = 0, 1, 0, []
    while c < n:
        if n < 3:
            arr.append(a * a)
            rez += arr[z]
        else:
            if c < 2:
                arr.append(a * a)
                rez += arr[z]
            else:
                arr.append(a)
                rez *= arr[z]
        c += 1
        z += 1
    return rez
print(power(a, n))