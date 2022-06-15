n = int(input())
s = int(input())

x = input().split(' ')
for i,ele in enumerate(x):
    x[i] = int(ele)
out = 0

for i in range(len(x)):
    soma = 0

    for e in x[i:]:
        soma += e
        if soma > s:
            break
        elif soma == s:
            out += 1

print(out)