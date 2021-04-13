t1 = list(map(int, input().split(':')))
t2 = list(map(int, input().split(':')))

s1 = t1[0]*3600+t1[1]*60
s2 = t2[0]*3600+t2[1]*60

interval = s2-s1
minute = interval // 60
if minute <= 10:
    print("Встреча состоится")
else:
    print("А надо было раньше")