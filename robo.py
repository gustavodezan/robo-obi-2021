pos = 0 # posição inicial
total = 0 # tempo total

# inputs
n,c,s = [int(x) for x in input().split()]
comm = [int(x) for x in input().split()]

s -= 1 # como pos inicia em 0, a posição desejada "s" é reduzida em 1

# sempre que a posição atual for igual à posição desejada, o tempo total é aumentado em 1
if pos == s:
    total += 1

for i in range(c):
    pos = (pos+comm[i])%n # a estação é circular então a posição atual é encontrada por (pos + valor do comando) % número de comandos recebidos
    if pos == s:
        total += 1

print(total)