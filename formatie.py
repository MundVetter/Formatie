from itertools import permutations

choices = ["alleen Dimitry", "alleen Felix", "geen van beide", "Dimitry en Felix"]
pref = []
for i in range(len(choices)):
    pref.extend(permutations(choices, i + 1))
print("Volgorde x: 1e voorkeur -> 2e voorkeur -> 3e voorkeur -> 4e voorkeur")
for i, r in enumerate(pref):
    print(f"Volgorde {i}: {' -> '.join(r)}")