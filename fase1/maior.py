n = int(input())
m = int(input())
s = int(input())

candidatos = []

for i in range(n, m):
    soma = i//10000+(i%10000)//1000+(i%1000)//100+(i%100)//10+(i%10)

    if soma == s:
        candidatos.append(i)

candidatos.sort()
candidatos.reverse()

if len(candidatos) == 0:
    print(-1)
else:
    print(candidatos[0])