import random

szam = random.random()
print(szam)

kocka = int(random.random()*6)+1
print(kocka)

kocka = random.randint(1, 6)

gyumolcsok = ["alma", "barack", "citrom", "dinnye", "eper", "füge"]

gyumolcs = random.choice(gyumolcsok)

random.shuffle(gyumolcsok)

minta = random.sample(gyumolcs, 3)
