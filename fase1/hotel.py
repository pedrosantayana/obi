d = int(input())
a = int(input())
n = int(input())

y=n

if y >= 16:
    y=15

diarias = 32-n
r = (d+(y-1)*a)*diarias

print(r)