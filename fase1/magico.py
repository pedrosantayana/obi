n = int(input())

quadrado = []

for i in range(n):
    linha = input()
    v = []
    for j in linha.split():
        v.append(int(j))

    quadrado.append(v)

correto = 0

for l in quadrado:
    if not 0 in l:
        va = 0
        for num in l:
            va += num
        
        correto = va
        break


out_linha = 0
out_coluna = 0
out = 0
for i, linha in enumerate(quadrado):
    if not 0 in linha:
        pass
    else:
        out_linha = i+1
        out_coluna = indexOf(linha, 0)+1
        r = 0
        for num in linha:
            r += num
        out = correto-r
        break

print(out)
print(out_linha)
print(out_coluna)