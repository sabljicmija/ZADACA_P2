import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

rjecnik = {}

for ime in imena:
    rjecnik[ime] = random.randint(1, 5)

ocjene = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

for ocjena in rjecnik.values():
    ocjene[ocjena] += 1

broj_prolaznih = sum(ocjene[ocjena] for ocjena in ocjene if ocjena > 1)
postotak_prolaznosti = (broj_prolaznih / len(imena)) * 100

print(ocjene)
print(f"Postotak prolaznosti: {postotak_prolaznosti}%")
