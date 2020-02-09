from time import sleep
print('{:=^40}'.format('Contagem Regressiva'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{:=^40}'.format('START'))