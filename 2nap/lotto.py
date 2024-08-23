import random

lottoszamok = []

while len(lottoszamok) < 5:
    ujszam = random.randint(1, 91)
    if (ujszam not in lottoszamok):
        lottoszamok.append(ujszam)
print(lottoszamok)


lottoszamok = []
print(sorted(random.sample(range(1, 91), 5)))
